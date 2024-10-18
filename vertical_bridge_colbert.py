import pdfplumber
import os,sys,re
from datetime import datetime
from langchain.text_splitter import CharacterTextSplitter,TokenTextSplitter,RecursiveCharacterTextSplitter
from langchain.schema import Document
from tqdm import tqdm
import numpy as np
import pandas as pd
import time
import json,uuid
import string
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate,HumanMessagePromptTemplate
from sentence_transformers import SentenceTransformer, util
import torch
from langchain_community.llms import Ollama
from flask import Flask, render_template,request,redirect,session, send_file,send_from_directory,url_for,flash
from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import LLMChain
from ragatouille import RAGPretrainedModel
from collections import defaultdict,OrderedDict
import vb_parser as pypar
import vb_prompts as pty
from json import JSONDecodeError


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" 



textfile = 'improper_response.txt'
llm_model = Ollama(model="llama3.1:8b",temperature=0,num_ctx = 10000)
RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")

app = Flask(__name__)

def log_exception(e, func_name, logfile):#function to log exceptions
    exc_type, exc_obj, tb = sys.exc_info()
    lineno = tb.tb_lineno
    error_message = f"\nIn {func_name} LINE.NO-{lineno} : {exc_obj}"
    with open(logfile, 'a', encoding='utf-8') as fp:
        fp.writelines(error_message)
        
def processLogger(process,logfile):
    with open(logfile,'a',encoding='utf-8') as fp:
        fp.writelines(f'\n{datetime.now()} {process}')

@app.route("/download/<path:filename>")
def download(filename):
    safe_path=filename
    return send_file(safe_path,as_attachment=True)

def remove_single_quotes_outside_substrings(s, substrings,logfile):
    try:  
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
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py remove_single_quotes_outside_substrings", logfile)
        return None


def convert_to_dict(dict_str,logfile):
    try:
        substrings_to_allow = ["'{'", "'}'", "':'", "','", "''", "' '","' {'","'} ,","' :'","': '","', '","' ,'","{'","'}"]
        single_quotes_and_apostrophes = ["‘", "’", "'", "’", "’"]
        
        # Replace each type of single quote and apostrophe with the straight single quote (')
        for char in single_quotes_and_apostrophes:
            if isinstance(dict_str, str):
                print("dict_str : ",dict_str,type(dict_str))
                dict_str = dict_str.replace(char, "'")
        if isinstance(dict_str, str):
            new_str = remove_single_quotes_outside_substrings(dict_str, substrings_to_allow,logfile)
            print('new str',new_str)
            json_string = new_str.replace("'", '"')
        else:
            if isinstance(dict_str, dict):
                json_string = dict_str
        # Convert the cleaned string to a dictionary
        try:
            return json.loads(json_string)
        except (json.JSONDecodeError, TypeError) as e:
            print(f"Error converting string to dictionary: {e}")
            log_exception(e, "In app.py wordCordinates", logfile)               
            
            return None
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py convert_to_dict", logfile)
        return None

def generate_key(index,logfile):
    try:
        alphabet = string.ascii_lowercase
        base = len(alphabet)
        key = ""
        while index >= 0:
            index, remainder = divmod(index, base)
            key = alphabet[remainder] + key
            index -= 1
        return key
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py generate_key", logfile)
        return key
    
def merge_paragraphs(blocks, line_spacing_threshold,logfile):
    try:   
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
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py merge_paragraphs", logfile)
        return paragraphs

def extract_paragraphs_from_pdf(pdf_path,logfile):
    all_paragraphs = []
    header_threshold=20
    line_spacing_threshold=5
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
            #for page_num, page in enumerate(range(5)):
                page_height = page.height
                # Extract words with positions
                blocks = page.extract_words()
                # Filter out potential headers based on a threshold
                filtered_blocks = [block for block in blocks if not block['top'] < header_threshold ]
                # Merge paragraphs
                paragraphs = merge_paragraphs(filtered_blocks, line_spacing_threshold,logfile)
                # Add page number to each paragraph
                for para in paragraphs:
                    all_paragraphs.append({
                        'text': para,
                        'page_number': page_num + 1  # Page numbers are 1-based
                    })
    except Exception as e:
        print(f"Error processing PDF: {e}")
        log_exception(e, "In vertical_bridge_colbert.py extract_paragraphs_from_pdf", logfile)
    
    return all_paragraphs


def split_paragraph(paragraph, text_splitter,logfile):
    try: 
        # Create a Document object
        document = Document(page_content=paragraph)
        
        # Use text_splitter to split the document
        try:
            chunks = text_splitter.split_documents([document])
        except Exception as e:
            print('Error while splitting documents:', e)
            return []
        
        # Debug: Check the length and content of the chunks
        print('Number of chunks:', len(chunks))
            
        return chunks
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py split_paragraph", logfile)

    
def findResponses(query,text,logfile):
    try:  
        response = llm_model.generate(
                prompts=[f"Query: {query}\nYText: {text}"]
            )
        return response
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py split_paragraph", logfile)

def mergeJson(result,logfile):
    try: 
        output=[]
        for data in result:
            for res in data:
                if res:
                    output.append(res)
        return output
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py mergeJson", logfile)

def is_valid(s,blocklist,logfile):
    try:   
        # Filter out non-alphabetic characters and check if the rest are uppercase
        alphabetic_chars = ''.join(filter(str.isalpha, s))
        return alphabetic_chars not in blocklist and alphabetic_chars != ''
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py is_valid", logfile)
    

def extract_entities(pdf_file_path,logfile):
    filename = os.path.basename(pdf_file_path)
    basename, _ = os.path.splitext(filename)
    answerfile = 'answer_for_3.1_new' + basename+'.json'
    paragraphs = extract_paragraphs_from_pdf(pdf_file_path,logfile)
    file_entities = []
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=3500, chunk_overlap=150)
    

    # Initialize an empty dictionary
    com_dict = {}
    outer = 0

    MAX_PARAGRAPH_LENGTH = 7000

    # Flag to track the current key
    current_key = None

    headtxt = {}
    current_head = None
    outer_head = 'First_Heading_Text'
    upper = 0
    blocklist = ['BETWEEN','INBETWEEN','AMONG','WITH','AND','TENANT','LANDLORD']
    try: 
        for para in paragraphs:
            if para['text'].isupper() and is_valid(para['text'],blocklist,logfile):
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
                    headtxt[current_head]['headtext'].append(para['text'])
                    headtxt[current_head]['pages'].append(para['page_number'])
            else:
                upper = 0
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
                headtxt[current_head]['headtext'].append(para['text'])
                headtxt[current_head]['pages'].append(para['page_number'])
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py extract_entities -- headtxt assiging", logfile)
    
    try:
        
        for head in headtxt:
            outer = 0
            current_key = None
            for i in range(len(headtxt[head]['headtext'])):
                para = headtxt[head]['headtext'][i]     
                page_number = headtxt[head]['pages'][i]    
                # Check if the paragraph matches the pattern        
                match = re.match(r'^[a-zA-Z0-9]\d*\.([a-zA-Z0-9]\d*)?\s', para)        
                if match:            
                    # Extract the key from the regex match   
                    base_key = head + '_' + match.group(0)                
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
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py extract_entities -- com_dict assiging", logfile)
    try:
        
        keys_to_check = list(com_dict.keys())
        for key in keys_to_check:
            section_text = com_dict[key]['section']
            if len(section_text) < 250 :
                t = int(len(section_text) / 500)
                for i in range(t):
                    section_text += '\n' + section_text
            elif len(section_text) > MAX_PARAGRAPH_LENGTH:
                # Split the paragraph into chunks and update the dictionary
                chunks = split_paragraph(section_text, text_splitter, logfile)
                # Remove the original entry
                # Add the chunks to the dictionary with new keys
                for index, chunk in enumerate(chunks):
                    new_key = f"{key}{generate_key(index,logfile)}"
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
        entity_class = pypar.entity_class
        queries = pty.queries
        model_queries = pty.model_queries
        model_formats = pty.model_formats
        model_answers = []
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py extract_entities -- after com_dict assiging till rag indexing", logfile)
    for i in range(len(queries)):
        try:
            query = queries[i]
            all_pages = []
            all_unique_pages = []
            top_chunks = {}
            results = RAG.search(query=query, k=7)
            final_text = ''
            final_text += com_dict['Lease_Page_1_Details']['section'] + '\n\n' + 'The above content is from page ' + str(com_dict['Lease_Page_1_Details']['page_no']) + '\n\n'
            for text in results:
                if text['passage_id'] not in top_chunks:
                    top_chunks[text['document_id']] = text['content']
                    all_pages.append(text['document_id'])
                    all_unique_pages.append(text['document_id'])
                    final_text += com_dict[text['document_id']]['section'] + '\n\n' + 'The above content is from page ' + str(com_dict[text['document_id']]['page_no']) + '\n\n'
                    
            unique_pages = list(OrderedDict.fromkeys(all_pages))
            top_5_pages = unique_pages[:5]
            #print('top_5_pages',top_5_pages)
            model_answer = []
            ct = 1
            entity_answer = []
            parser = JsonOutputParser(pydantic_object = pypar.entity_class[i])
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
                            f"Question: {model_queries[i]}\n\n"
                        )

            #print('Lenght model text',len(final_text))
            #print('Lenght of model text words',len(final_text.split(' ')))
        except Exception as e:
            log_exception(e, "In vertical_bridge_colbert.py extract_entities -- after rag indexing till prompting", logfile)
        try:
            ollama_result = chain.invoke({"query_text": query_text})
            entity_answer.append(ollama_result)
##            try:
##                entity_answer.append(ollama_result)
##            except Exception as e:
##                log_exception(e, "In vertical_bridge_colbert.py extract_entities -- parser model result appending", logfile)

        except Exception as e:
            log_exception(e, "In vertical_bridge_colbert.py extract_entities -- parser model not worked", logfile)
            print("error parser model:",e)
            try:
                #print("final_text : ", final_text)
                res = findResponses(model_prompt, final_text, logfile)
                for generation_chunk in res.generations:
                    for generation in generation_chunk:
                        ollama_result = generation.text
            except Exception as e:
                ollama_result = 'None'
                log_exception(e, "In vertical_bridge_colbert.py extract_entities -- model not worked", logfile)
                print("error parser model:",e)

        # Skipping invalid JSON
        try:
            
            if isinstance(ollama_result, str):
                json_string = ollama_result.replace("'", '"')
                json_loads = json.loads(json_string)
                entity_answer.append(json_loads)

            elif isinstance(ollama_result, dict):
                    json_string = ollama_result
                    #json_loads = json.loads(json_string)
                    entity_answer.append(json_string)
            
                
        except JSONDecodeError as e:
            print('JSONDecodeError', e)
            log_exception(e, "In vertical_bridge_colbert.py extract_entities -- JSONDecodeError, skipping this json", logfile)
            # Skip invalid JSON and continue to the next one
        except Exception as e:
            print('Cannot add1', e)
            log_exception(e, "In vertical_bridge_colbert.py extract_entities -- Other model answer json loads error", logfile)
            try:
                response_dict = convert_to_dict(ollama_result, logfile)
                entity_answer.append(response_dict)
            except Exception as e:
                log_exception(e, "In vertical_bridge_colbert.py extract_entities -- model answer json conversion error", logfile)
                print('Cannot add2', e)
                try:
                    entity_answer.append(ollama_result)
                except Exception as e:
                    log_exception(e, "In vertical_bridge_colbert.py extract_entities -- Nothing worked at model calling", logfile)
                    print('Cannot add3', e)
                    entity_answer.append("")
##        try :
##            ollama_result = chain.invoke({"query_text": query_text})
##            
##            try:
##                entity_answer.append(ollama_result)
##            except Exception as e:
##                log_exception(e, "In vertical_bridge_colbert.py extract_entities -- parser model result appending", logfile)
##        except Exception as e:
##            log_exception(e, "In vertical_bridge_colbert.py extract_entities -- parser model not worked", logfile)
##            try:
##                print("final_text : ",final_text)
##                res = findResponses(model_prompt,final_text,logfile)
##                for generation_chunk in res.generations:
##                    for generation in generation_chunk:
##                        ollama_result = generation.text
##            except Exception as e:
##                ollama_result = 'None'
##                log_exception(e, "In vertical_bridge_colbert.py extract_entities --  model not worked", logfile)
##            try:
##                json_string = ollama_result.replace("'", '"')
##                json_loads = json.loads(json_string)
##                entity_answer.append(json_loads)
##            except Exception as e:
##                log_exception(e, "In vertical_bridge_colbert.py extract_entities --  model answer json loads error ", logfile)
##                try :
##                    response_dict = convert_to_dict(ollama_result,logfile)
##                    entity_answer.append(response_dict)
##                except Exception as e:
##                    log_exception(e, "In vertical_bridge_colbert.py extract_entities --  model answer json conversion error", logfile)
##                    try:
##                        entity_answer.append(ollama_result)
##                    except Exception as e :
##                        log_exception(e, "In vertical_bridge_colbert.py extract_entities --  Nothing worked at model calling ", logfile)
##                        print('Can not add',e)
##                        entity_answer.append("")
            
##        print('entity_answer ',entity_answer)
##        print('#'*150)
##        print()
    try:
                
        # Write the JSON data to a file
        with open(answerfile, 'w') as file:
            json.dump(file_entities, file, indent=4)  # indent=4 for pretty-printing
        
        print(f"Data successfully written to {answerfile}")
        try:
            result=json.loads(open(answerfile,"r").read())
            output = mergeJson(result,logfile)
            #print('output flattened')
            for entity_output in output :
                if('Position' in entity_output):
                    entity_output['Position'] = list(OrderedDict.fromkeys(entity_output['Position']))
                elif ('PageNum' in entity_output):
                    entity_output['PageNum'] = list(OrderedDict.fromkeys(entity_output['PageNum']))
                    page_list = entity_output['PageNum']
                    page_list_1 = [page for page in page_list if page.isnumeric()]
                    entity_output['PageNum'] = list(OrderedDict.fromkeys(page_list_1))
            print('returning the output successfully')
            return output
        except Exception as e :
            print(f"Failed to Flatten JSON: {e}")
            log_exception(e, "In vertical_bridge_colbert.py extract_entities --  flatten error ", logfile)
            with open(logfile, 'a', encoding='utf-8') as fp:
                fp.write(str(e))
            

    except json.JSONDecodeError as e:
        log_exception(e, "In vertical_bridge_colbert.py extract_entities --  json loads error ", logfile)
        print(f"Failed to decode JSON: {e}")
    except IOError as e:
        log_exception(e, "In vertical_bridge_colbert.py extract_entities --  can not write in file", logfile)
        print(f"Failed to write to file: {e}")
    return file_entities



with open("config.json", "r") as cf:
    data = json.load(cf)
folder_path = data["folder_path"]


@app.route('/',methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    
@app.route('/start_Rag',methods=['GET', 'POST'])
def start_Rag():
    try:
        all_data = []
        if request.method == 'GET':
            return render_template('upload.html')
        start = datetime.now()
        uuidName=str(uuid.uuid4())
        logfile = f"logs/{uuidName}.txt"
        print("logfile : ",logfile)
        processLogger("started",logfile)
        os.mkdir(f"PDFFILE/{uuidName}")
        download_directory = f"PDFFILE/{uuidName}"
        files = request.files.getlist('files[]')

        for file in files:
            if file and file.filename.endswith('.pdf'):  # Check for PDF files
                # Save each file
                filename = file.filename
                file.save(os.path.join(download_directory, filename))
        check_pdf = download_directory
        
        df_dict = {
                'File_Name':[],
                'Entity_Name':[],
                'Entity':[],
                'Position':[],
                'Page':[]
            }
        for file_name in os.listdir(check_pdf):
            pdf_path = os.path.join(check_pdf,file_name)
            basename, _ = os.path.splitext(file_name)
            print(f'Processing file: {pdf_path}')
            final_answers = extract_entities(pdf_path,logfile)
            all_data.append(final_answers)
            for answers in final_answers :
                entity_name = []
                entity =[]
                position = []
                page = []
                for answer in answers:
                    if 'Position' in  str(answer):
                        for i in range(len(answers[answer])):
                            try:
                                position.append(answers[answer][i])
                            except Exception as e:
                                position.append(answers[answer])
                    elif 'PageNum' in str(answer):
                        for i in range(len(answers[answer])):
                            try:
                                page.append(answers[answer][i])
                            except Exception as e:
                                page.append(answers[answer])
                    else:
                        entity.append(str(answers[answer]))
                        entity_name.append(str(answer))
                for i in range(len(entity_name)):
                    df_dict['File_Name'].append(basename)
                    df_dict['Entity_Name'].append(entity_name[i])
                    df_dict['Entity'].append(entity[i])
                    df_dict['Position'].append(position)
                    df_dict['Page'].append(page)
        jsonFile = f"PDFFILE/{uuidName}.json"
        with open(jsonFile,'w') as f:
            json.dump(all_data,f,indent=4)
        print('all_data : \n',all_data)
        Id  = request.args.get('Id')
        df = pd.DataFrame(df_dict)
        grouped_df = df.groupby('Entity_Name').apply(lambda x: x).reset_index(drop=True)
        grouped_df.reset_index(inplace = True,names = 'S.No')
        excel_name = uuidName + "_data.xlsx"
        excelFilePath = os.path.join(download_directory,excel_name)
        grouped_df.to_excel(excelFilePath,index = False)
        end = datetime.now()
        print("total time : ",end-start)
        return redirect(url_for('download',filename=excelFilePath))
    except Exception as e:
        log_exception(e, "In vertical_bridge_colbert.py start_Rag", logfile)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9006)

