import pdfplumber
import os,sys,re
from datetime import datetime
from langchain.text_splitter import CharacterTextSplitter,TokenTextSplitter,RecursiveCharacterTextSplitter
from langchain.schema import Document
from tqdm import tqdm
import numpy as np
import time
import json
import string
#import warnings
#warnings.filterwarnings("ignore")
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate,HumanMessagePromptTemplate
from sentence_transformers import SentenceTransformer, util
import torch
from langchain_community.llms import Ollama
from flask import Flask, render_template,request
#from llama_index.llms.ollama import Ollama
from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser
#from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import LLMChain
from ragatouille import RAGPretrainedModel
from collections import defaultdict,OrderedDict
#import pydantic_parser_realserv_updated as pypar
#import realserv_prompts_entity_updated as pty
import pydantic_parser_realserv_section as pypar
import realserv_prompts_entity_section as pty
#import pydantic_parser_realserv as pypar
#import realserv_prompts_entity as pty
#import entity_1 as pty
#import parser_1 as pypar
#import New_set_entity as pty
#import New_set_parser as pypar

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" 

print('realserv_prompts_entity_updated entity count',len(pty.entity))
print('realserv_prompts_entity_updated queries count',len(pty.queries))
print('realserv_prompts_entity_updated model answers count',len(pty.model_formats))
print('pydantic_parser_realserv_updated class count',len(pypar.entity_class))


logfile = 'llama_rag.0log.txt'
textfile = 'improper_response.txt'
llm_model = Ollama(model="llama3.1:8b",temperature=0.2,num_ctx = 10000)
RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")

app = Flask(__name__)


def remove_single_quotes_outside_substrings(s, substrings):
    """
    Remove single quotes from the string `s` that are not part of specified substrings.

    Args:
    - s (str): The string from which to remove single quotes.
    - substrings (list of str): The substrings where single quotes are allowed.

    Returns:
    - str: The modified string with single quotes removed outside the specified substrings.
    """
    # Use a list to build the resulting string
    result = []
    i = 0
    length = len(s)

    while i < length:
        # Check if the current position matches any of the allowed substrings
        matched = False
        for substring in substrings:
            if s[i:i+len(substring)] == substring:
                result.append(substring)
                i += len(substring)
                matched = True
                break
        
        if not matched:
            # Remove single quotes that are not part of an allowed substring
            if s[i] == "'":
                # Skip the single quote
                i += 1
            else:
                # Append the current character to the result
                result.append(s[i])
                i += 1

    return ''.join(result)


def convert_to_dict(dict_str):
    # Replace single quotes around keys and values with double quotes
    # Ensuring that keys and values are properly handled
    '''dict_list_str = dict_str.split(" ")
    pattern = r'[a-zA-Z]\'[a-zA-Z]'
    #dict_list_str_1 = dict_list_str.split("")
    print("splitedd",dict_list_str) 
    for index, i in enumerate(dict_list_str):
        if '{' in i or ':' in i:
            continue
        elif "'" in i:
            if bool(re.search(pattern, i)):
                dict_list_str[index] = i.replace("'", '')
                print("updated ", dict_list_str[index])
            else:
                print('no need', i)

    
    new_str = ' '.join(dict_list_str)
    print('new str',new_str)'''
    print('old str',dict_str)
    substrings_to_allow = ["'{'", "'}'", "':'", "','", "''", "' '","' {'","'} ,","' :'","': '","', '","' ,'","{'","'}"]
    single_quotes_and_apostrophes = ["‘", "’", "'", "’", "’"]
    
    # Replace each type of single quote and apostrophe with the straight single quote (')
    for char in single_quotes_and_apostrophes:
        dict_str = dict_str.replace(char, "'")
    new_str = remove_single_quotes_outside_substrings(dict_str, substrings_to_allow)
    print('new str',new_str)
    json_string = new_str.replace("'", '"')
    # Convert the cleaned string to a dictionary
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error converting string to dictionary: {e}")
        with open(textfile, 'a', encoding='utf-8') as fp:
            fp.write('old str.........')
            fp.write('\n\n')
            fp.writelines(dict_str)
            fp.write('\n\n')
            fp.write('New str.........')
            fp.write('\n\n')
            fp.writelines(new_str)
            fp.write('\n\n')
            fp.write('##################################')
            fp.write('\n\n\n')
            
        
        return None

def generate_key(index):
    alphabet = string.ascii_lowercase
    base = len(alphabet)
    key = ""
    while index >= 0:
        index, remainder = divmod(index, base)
        key = alphabet[remainder] + key
        index -= 1
    return key
    
def merge_paragraphs(blocks, line_spacing_threshold):
    paragraphs = []
    current_paragraph = ""
    
    for i, block in enumerate(blocks):
        if not current_paragraph:
            current_paragraph = block['text']
        else:
            previous_block = blocks[i - 1]
            if block['top'] - previous_block['bottom'] < line_spacing_threshold:
                current_paragraph += " " + block['text']
            else:
                paragraphs.append(current_paragraph)
                current_paragraph = block['text']
    if current_paragraph:
        paragraphs.append(current_paragraph)
    
    return paragraphs

def extract_paragraphs_from_pdf(pdf_path, header_threshold=20, line_spacing_threshold=5):
    all_paragraphs = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_height = page.height
                # Extract words with positions
                blocks = page.extract_words()
                # Filter out potential headers based on a threshold
                filtered_blocks = [block for block in blocks if not block['top'] < header_threshold ]
                # Merge paragraphs
                paragraphs = merge_paragraphs(filtered_blocks, line_spacing_threshold)
                # Add page number to each paragraph
                for para in paragraphs:
                    all_paragraphs.append({
                        'text': para,
                        'page_number': page_num + 1  # Page numbers are 1-based
                    })
    except Exception as e:
        print(f"Error processing PDF: {e}")
    
    return all_paragraphs


def split_paragraph(paragraph, text_splitter):
    # Debug: Check the length and content of the input paragraph
    #print('Length of the input paragraph:', len(paragraph))
    #print('Input paragraph:', paragraph[:1000])  # Print the first 1000 characters for readability
    
    # Create a Document object
    document = Document(page_content=paragraph)
    #print('Type of Document object:', type(document))
    
    # Use text_splitter to split the document
    try:
        chunks = text_splitter.split_documents([document])
    except Exception as e:
        print('Error while splitting documents:', e)
        return []
    
    # Debug: Check the length and content of the chunks
    print('Number of chunks:', len(chunks))
    #print('Type of chunks:', type(chunks))
    
    # Print the content of the first chunk for verification (if available)
    
    return chunks

    
def findResponses(query,text):
    response = llm_model.generate(
            prompts=[f"Query: {query}\nYText: {text}"]
        )
    return response
    

def extract_entities(pdf_file_path):
    filename = os.path.basename(pdf_file_path)
    basename, _ = os.path.splitext(filename)
    answerfile = 'answer_for_3.1_new' + basename+'.json'
    paragraphs = extract_paragraphs_from_pdf(pdf_file_path)
    file_entities = {}
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=5000, chunk_overlap=500)
    

    # Initialize an empty dictionary
    com_dict = {}
    outer = 0

    MAX_PARAGRAPH_LENGTH = 10000

    # Flag to track the current key
    current_key = None

    headtxt = {}
    current_head = None
    outer_head = 'First_Heading_Text'
    upper = 0
    blocklist = ['BETWEEN','INBETWEEN','AMONG','WITH','AND','TENANT','LANDLORD']
    def is_valid(s):
        # Filter out non-alphabetic characters and check if the rest are uppercase
        alphabetic_chars = ''.join(filter(str.isalpha, s))
        return alphabetic_chars not in blocklist and alphabetic_chars != ''


    for para in paragraphs:
        #print(para['text'])
        if para['text'].isupper() and is_valid(para['text']):
            if upper == 1:
                if current_head == None:
                    current_head = outer_head
                    headtxt[outer_head] = {
                        'headtext' : [],
                        'pages':[]
                    }
                if current_head not in headtxt:                    
                    headtxt[current_head] = {                        
                        'headtext': [],                        
                        'pages': []                    
                    }
                #headtxt[current_head]['headtext'] += para['text'] + '\n\n'
                headtxt[current_head]['headtext'].append(para['text'])
                headtxt[current_head]['pages'].append(para['page_number'])
            elif upper == 0 and para['text'] != '' :
                upper = 1
                current_head = para['text']
                if current_head not in headtxt:                    
                    headtxt[current_head] = {                        
                        'headtext': [],                        
                        'pages': []                    
                    }
                #headtxt[current_head]['headtext'] += para['text'] + '\n\n'
                headtxt[current_head]['headtext'].append(para['text'])
                headtxt[current_head]['pages'].append(para['page_number'])
        else:
            upper = 0
            if current_head == None:
                current_head = outer_head
                headtxt[outer_head] = {
                    'headtext' : '',
                    'pages':[]
                }
            if current_head not in headtxt:                 
                headtxt[current_head] = {                        
                    'headtext': '',                        
                    'pages': []                    
                }
            #headtxt[current_head]['headtext'] += para['text'] + '\n\n'
            headtxt[current_head]['headtext'].append(para['text'])
            headtxt[current_head]['pages'].append(para['page_number'])


    '''for para_info in paragraphs:
        para = para_info['text']
        page_number = para_info['page_number']
        
        # Check if the paragraph matches the pattern
        match = re.match(r'^(\d+\.\d+)', para)
        if match:
            # Extract the key from the regex match
            base_key = match.group(1)
            if base_key not in com_dict:
                com_dict[base_key] = {
                    'section': '',
                    'page_no': []
                }
            current_key = base_key
            # Append the paragraph to the current entry
            com_dict[current_key]['section'] += '\n\n' + para
            if page_number not in com_dict[current_key]['page_no']:
                com_dict[current_key]['page_no'].append(page_number)
        else:
            # If current_key is set, append the paragraph to the existing entry
            if current_key is not None:
                # Ensure the current_key exists in the dictionary
                if current_key not in com_dict:
                    com_dict[current_key] = {
                        'section': '',
                        'page_no': []
                    }
                com_dict[current_key]['section'] += '\n\n' + para
                if page_number not in com_dict[current_key]['page_no']:
                    com_dict[current_key]['page_no'].append(page_number)'''
    '''for para_info in paragraphs:        
        para = para_info['text']        
        page_number = para_info['page_number']        
        # Check if the paragraph matches the pattern        
        match = re.match(r'^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)?\s', para)        
        if match:            
            # Extract the key from the regex match            
            base_key = match.group(0)    
            #print('base_key',base_key)            
            #print('%'*20)            
            outer=base_key            
            if base_key not in com_dict:                
                com_dict[base_key] = {                    
                    'section': '',                    
                    'page_no': []                
                }            
                current_key = base_key            
            # Append the paragraph to the current entry            
                com_dict[current_key]['section'] += para + '\n\n'            
                com_dict[current_key]['page_no'].append(page_number)            
            #if page_number not in com_dict[current_key]['page_no']:        
        elif outer == 0 :            
            outer_base_key = '0.0'            
            if outer_base_key not in com_dict:                
                com_dict[outer_base_key] = {                    
                    'section': '',                    
                    'page_no': []                
                }                        
            # Append the paragraph to the current entry            
            com_dict[outer_base_key]['section'] += para + '\n\n'            
            com_dict[outer_base_key]['page_no'].append(page_number)                        
        else:                                      
            # If current_key is set, append the paragraph to the existing entry            
            if current_key is not None:                
                # Ensure the current_key exists in the dictionary                
                if current_key not in com_dict:                    
                    com_dict[current_key] = {                        
                        'section': '',                        
                        'page_no': []                    
                    }                
                com_dict[current_key]['section'] += '\n\n' + para                
                com_dict[current_key]['page_no'].append(page_number)'''
    for head in headtxt:
        print(head)
        print('\n')
        print('len',len(headtxt[head]['headtext']))
        print('\n')
        
        outer = 0
        current_key = None
        for i in range(len(headtxt[head]['headtext'])):
            para = headtxt[head]['headtext'][i]     
            #print('para',para)
            page_number = headtxt[head]['pages'][i]    
            # Check if the paragraph matches the pattern        
            match = re.match(r'^[a-zA-Z0-9]\d*\.([a-zA-Z0-9]\d*)?\s', para)        
            if match:            
                # Extract the key from the regex match   
                base_key = head + '_' + match.group(0)    
                print('base_key',base_key)            
                print('%'*20)            
                outer=base_key            
                if base_key not in com_dict:                
                    com_dict[base_key] = {                    
                        'section': '',                    
                        'page_no': []                
                    }            
                    current_key = base_key            
                # Append the paragraph to the current entry            
                    com_dict[current_key]['section'] += head + '\n\n' + para + '\n\n'            
                    com_dict[current_key]['page_no'].append(page_number)            
                #if page_number not in com_dict[current_key]['page_no']:        
            elif outer == 0 :            
                outer_base_key = head + '_' + '0.0'            
                if outer_base_key not in com_dict:                
                    com_dict[outer_base_key] = {                    
                        'section': '',                    
                        'page_no': []                
                    }                        
                # Append the paragraph to the current entry            
                com_dict[outer_base_key]['section'] += para + '\n\n'            
                com_dict[outer_base_key]['page_no'].append(page_number)                        
            else:                                      
                # If current_key is set, append the paragraph to the existing entry            
                if current_key is not None:                
                    # Ensure the current_key exists in the dictionary                
                    if current_key not in com_dict:                    
                        com_dict[current_key] = {                        
                            'section': '',                        
                            'page_no': []                    
                        }                
                    com_dict[current_key]['section'] += '\n\n' + para                
                    com_dict[current_key]['page_no'].append(page_number)
        print('^'*20)



    # Print the results
    '''for key, value in com_dict.items():
        print(f"{key}:")
        print(f"  Section: {value['section']}")
        print(f"  Page No: {value['page_no']}")
        print('--' * 20)'''


    keys_to_check = list(com_dict.keys())
    for key in keys_to_check:
        section_text = com_dict[key]['section']
        if len(section_text) < 250 :
            print('the section is small',section_text)
            print('@'*20)
            t = int(len(section_text) / 500)
            for i in range(t):
                section_text += '\n' + section_text
        elif len(section_text) > MAX_PARAGRAPH_LENGTH:
            # Split the paragraph into chunks and update the dictionary
            chunks = split_paragraph(section_text, text_splitter)
            # Remove the original entry
            # Add the chunks to the dictionary with new keys
            for index, chunk in enumerate(chunks):
                new_key = f"{key}{generate_key(index)}"
                com_dict[new_key] = {
                    'section': chunk.page_content,
                    'page_no': com_dict[key]['page_no']
                }
            del com_dict[key]

    with pdfplumber.open(pdf_file_path) as pdf:
        # Extract the first page
        first_page = pdf.pages[0]
        
        
        # Extract text from the first page
        first_page_text = first_page.extract_text()
        first_page_text += 'Page 1' + '\n'
        com_dict['Lease_Page_1_Details'] = {
                            'section': first_page_text,
                            'page_no':[1]
                            }
    

    all_paragraphs_list = []
    keys_list = []

    for key, value in com_dict.items():
        all_paragraphs_list.append(value['section'])
        keys_list.append(key)

    RAG.index(
            collection=all_paragraphs_list,
            document_ids = keys_list,
            index_name="colbert_realserv",
            overwrite_index = True,
            max_document_length=512,
            split_documents=True,
            use_faiss=True 
        )
    entity = pty.entity
    entity_class = pypar.entity_class
    queries = pty.queries
    model_formats = pty.model_formats
    model_answers = []
    for i in range(len(queries)):
        print('i',i)
        '''if i == 10 or i == 14 or i == 15 or i == 16:
            print('escape because i is :',i)
            continue'''
        query = queries[i]
        file_entities[entity[i]] = []
        all_pages = []
        all_unique_pages = []
        top_chunks = {}
        results = RAG.search(query=query, k=7)
        final_text = ''
        #print('resultss',results)
        for text in results:
            if text['passage_id'] not in top_chunks:
                top_chunks[text['document_id']] = text['content']
                all_pages.append(text['document_id'])
                all_unique_pages.append(text['document_id'])
                final_text += com_dict[text['document_id']]['section'] + '\n\n' + 'The above content is from page ' + str(com_dict[text['document_id']]['page_no']) + '\n\n'
                
        unique_pages = list(OrderedDict.fromkeys(all_pages))
        #print('all pages',all_pages)
        # Get the top 5 unique pages
        top_5_pages = unique_pages[:5]
        print('top_5_pages',top_5_pages)
        '''final_text = ''
        for passage_id in all_results:
          final_text = final_text + '.' + all_results[passage_id]'''
        #print('len of final text',len(final_text))
        #print('result!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',final_text)
        #print('start : ', datetime.now())
        #print('model_query: ',model_queries[i])
        model_answer = []
        ct = 1
        '''for page in top_5_pages:
            page_ans = {}
            entity_chunk = []
            final_text = com_dict[page]['section']
            #print('final_text',final_text)
            #print('-'*30)
            page_ans['page']=page
            page_ans['chunks']=final_text
            entity_answer = []
            #print('ct is :',ct)
            parser = JsonOutputParser(pydantic_object = pypar.entity_class[i])
            #parser = PydanticOutputParser(pydantic_object=entity[i])
            #print(parser.get_format_instructions())
            query_text = f"Question: {query} Context: {final_text}"
            prompt = PromptTemplate(
                template=(
                    "Your ability to answer  the questions accurately is essential for effective "
                    "lease agreement analysis. Pay close attention to the lease agreement's language, "
                    "structure, and any cross-references to ensure a comprehensive and precise extraction of "
                    "information. Do not use prior knowledge or information from outside the context to answer the "
                    "questions. Only use the information provided in the context to answer the questions."
                    "Do not include any explanation in the reply. Only include the answer for the question in the reply."
                    "Do not give any summary for the given content only give the answer for the question given."
                    "Strictly avoid using single quotes other than straight single quotes and asterisk in the response."
                    "Ensure that the reply follows the JSON format provided below (NO PREAMBLE and NO POSTAMBLE):\n\n"
                    "{format_instructions}\n\n"
                    "Context: {query_text}\n\n"
                    ),
                input_variables=["query_text"],
                partial_variables={"format_instructions": parser.get_format_instructions()},
            )
            chain = prompt | llm_model | parser

            model_prompt = (
                            f"Your ability to answer the questions accurately is essential for effective "
                            f"lease agreement analysis. Pay close attention to the lease agreement's language, "
                            f"structural details, and any cross-references to ensure a comprehensive and precise extraction of "
                            f"information. Do not use prior knowledge or information from outside the context to answer the questions. "
                            f"Only use the information provided in the context to answer the questions.\n\n"
                            f"Do not include any explanations or summaries in your reply. Only include the answer to the question.\n\n"
                            f"Strictly avoid using single quotes other than straight single quotes in the response."
                            f"Ensure that your reply follows the JSON format provided below with NO Preambles and postambles:\n\n"
                            f"{model_formats[i]}\n\n"
                            f"Question: {query}\n\n"
                        )

            
            try :
                ollama_result = chain.invoke({"query_text": query_text})
                
                try:
                    entity_answer.append(ollama_result)
                    #print('type of result appended',type(ollama_result))
                except Exception as e:
                    #print('error with json dumps',e)
                    try :
                        entity_answer.append(ollama_result)
                        #print('type of result appended',type(ollama_result))
                    except Exception as e:
                            print('Error occured!!')
            
            except Exception as e:
                #print('error with parser mothod',e)
                #res = findResponses(model_queries[i],final_text)
                res = findResponses(model_prompt,final_text)
                for generation_chunk in res.generations:
                    for generation in generation_chunk:
                        ollama_result = generation.text
                        #print('result form ollama_result 2',ollama_result)
                        #print('type of result',type(ollama_result))
                        #print('\n\n')
                try:
                    #json_string = json.dumps(ollama_result, indent=4)
                    #entity_answer.append(json_string)
                    json_string = ollama_result.replace("'", '"')
                    #print('replaced string',json_string)
                    json_loads = json.loads(json_string)
                    entity_answer.append(json_loads)
                    #print("type of ollama2 :",json_string)
                    #entity_answer.append(ollama_result)
                    #print('type of result appended',type(json_string))
                except Exception as e:
                    #print('error with json loads')
                    try :
                        response_dict = convert_to_dict(ollama_result)
                        entity_answer.append(response_dict)
                        #print('type of result appended',type(ollama_result))
                    except Exception as e:
                        #print('Error occured!!')
                        try:
                            entity_answer.append(ollama_result)
                            #print('type of result appended',type(ollama_result))
                        except Exception as e :
                            print('Can not add',e)
                            entity_answer.append("")
                
            print('entity_answer ',entity_answer)
            print('###################################'+'\n\n')
            page_ans['Answers']=entity_answer
            #print('page_answer ',page_ans)
            #print('###################################'+'\n\n')
            file_entities[entity[i]].append(page_ans)
            ct = int(ct) + 1'''
        entity_answer = []
        #print('ct is :',ct)
        parser = JsonOutputParser(pydantic_object = pypar.entity_class[i])
        #parser = PydanticOutputParser(pydantic_object=entity[i])
        #print(parser.get_format_instructions())
        query_text = f"Question: {query} Context: {final_text}"
        prompt = PromptTemplate(
            template=(
                "Your ability to answer  the questions accurately is essential for effective "
                "lease agreement analysis. Pay close attention to the lease agreement's language, "
                "structure, and any cross-references to ensure a comprehensive and precise extraction of "
                "information. Do not use prior knowledge or information from outside the context to answer the "
                "questions. Only use the information provided in the context to answer the questions."
                "Do not include any explanation in the reply. Only include the answer for the question in the reply."
                "Do not give any summary for the given content only give the answer for the question given."
                "Strictly avoid using single quotes other than straight single quotes and asterisk in the response."
                "Ensure that the reply follows the JSON format provided below (NO PREAMBLE and NO POSTAMBLE):\n\n"
                "{format_instructions}\n\n"
                "Context: {query_text}\n\n"
                ),
            input_variables=["query_text"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        chain = prompt | llm_model | parser

        model_prompt = (
                        f"Your ability to answer the questions accurately is essential for effective "
                        f"lease agreement analysis. Pay close attention to the lease agreement's language, "
                        f"structural details, and any cross-references to ensure a comprehensive and precise extraction of "
                        f"information. Do not use prior knowledge or information from outside the context to answer the questions. "
                        f"Only use the information provided in the context to answer the questions.\n\n"
                        f"Do not include any explanations or summaries in your reply. Only include the answer to the question.\n\n"
                        f"Strictly avoid using single quotes other than straight single quotes in the response."
                        f"Ensure that your reply follows the JSON format provided below with NO Preambles and postambles:\n\n"
                        f"{model_formats[i]}\n\n"
                        f"Question: {query}\n\n"
                    )


        try :
            ollama_result = chain.invoke({"query_text": query_text})
            
            try:
                entity_answer.append(ollama_result)
                #print('type of result appended',type(ollama_result))
            except Exception as e:
                #print('error with json dumps',e)
                try :
                    entity_answer.append(ollama_result)
                    #print('type of result appended',type(ollama_result))
                except Exception as e:
                        print('Error occured!!')

        except Exception as e:
            #print('error with parser mothod',e)
            #res = findResponses(model_queries[i],final_text)
            res = findResponses(model_prompt,final_text)
            for generation_chunk in res.generations:
                for generation in generation_chunk:
                    ollama_result = generation.text
                    #print('result form ollama_result 2',ollama_result)
                    #print('type of result',type(ollama_result))
                    #print('\n\n')
            try:
                #json_string = json.dumps(ollama_result, indent=4)
                #entity_answer.append(json_string)
                json_string = ollama_result.replace("'", '"')
                #print('replaced string',json_string)
                json_loads = json.loads(json_string)
                entity_answer.append(json_loads)
                #print("type of ollama2 :",json_string)
                #entity_answer.append(ollama_result)
                #print('type of result appended',type(json_string))
            except Exception as e:
                #print('error with json loads')
                try :
                    response_dict = convert_to_dict(ollama_result)
                    entity_answer.append(response_dict)
                    #print('type of result appended',type(ollama_result))
                except Exception as e:
                    #print('Error occured!!')
                    try:
                        entity_answer.append(ollama_result)
                        #print('type of result appended',type(ollama_result))
                    except Exception as e :
                        print('Can not add',e)
                        entity_answer.append("")
            
        print('entity_answer ',entity_answer)
        print('###################################'+'\n\n')
        #print('page_answer ',page_ans)
        #print('###################################'+'\n\n')
        file_entities[entity[i]].append(entity_answer)
    #print('file_entities',file_entities)
    #print('\n\n')
    #print('type of file_entities',type(file_entities))
    #print('*********************************************************************************')
    try:
        
        #data = json.loads(file_entities)
        
        # Write the JSON data to a file
        with open(answerfile, 'w') as file:
            #file.write(f'{json.dumps(file_entities)}')
            json.dump(file_entities, file, indent=4)  # indent=4 for pretty-printing
        
        print(f"Data successfully written to {answerfile}")

    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    except IOError as e:
        print(f"Failed to write to file: {e}")
    '''with open(answerfile, 'a') as file:
        json.dump(file_entities, file, indent=4)'''
    return 0

'''def start_Rag(path):
    print('start : ', datetime.now())
    print(f'Processing file: {path}')
    final_pages = extract_entities(path)
    print('End : ', datetime.now())
    

#start_Rag('./PDF_filess/PeterbiltIllinoisVJ.pdf')
#start_Rag('./PDF_filess/Concentric_SL6_FLA_Lease_2180PremierRow (Executed).pdf')
start_Rag('./PDF_filess/NEWPORT_COAST_NEWPORT BEAUTY SALON.pdf')
#start_Rag('./PDF_filess/Lease Agreement with Guaranty - 9-30-2021.pdf')
#start_Rag('./PDF_filess/WOODBURY_TOWN_CENTER-ROCK_N_ROAD_CYCLERY.pdf')'''


with open("config.json", "r") as cf:
    data = json.load(cf)
folder_path = data["folder_path"]

@app.route('/',methods=['GET', 'POST'])
def start_Rag():
    folderName = request.args.get('folderName')
    file_name = request.args.get('filename')
    Id  = request.args.get('Id')
    check_pdf = os.path.join(folder_path,folderName)
    if file_name in os.listdir(check_pdf):
        pdf_path = os.path.join(check_pdf,file_name)

        print('start : ', datetime.now())
        print(f'Processing file: {pdf_path}')
        final_pages = extract_entities(pdf_path)
        print('End : ', datetime.now())
    return "done"

if __name__ == "__main__":
    app.run(port=9003)

