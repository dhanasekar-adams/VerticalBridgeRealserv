from pydantic import BaseModel,Field
from datetime import datetime


class Landlord_Entity_Name (BaseModel):

    Landlord_Entity_Name : str = Field(description = "Identify the Landlord Entity Name as specified in the Ground Lease section of the latest document."
                                       "Provide the exact name of the landlord entity responsible under the ground lease."
                                       "If No valid answer is found then return NA",
                                       max_length = 200
                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class Execution_Date (BaseModel):
    Execution_Date : str = Field(description = "Identify the Execution Date of this lease."
                                 "Search for terms like 'Execution Date,' 'Date of Execution,' or similar phrases that indicate when the lease was signed by the parties."
                                 "Output format should be mm/dd/yyyy."
                                 "If No valid answer is found then return NA",
                                 max_length = 60
                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Initial_Lease_Commencement_Date (BaseModel):
    Initial_Lease_Commencement_Date : str = Field(description = "Identify and extract the 'Initial Lease Commencement Date' from the lease document."
                                                  "This date should reflect the official start of the lease term as specified in the document,"
                                                  "taking into account any stated conditions or specific events that trigger the commencement of the lease."
                                                  "If the commencement date is not explicitly stated, check for references to lease signing, delivery of possession, or any conditions that indicate when the lease term begins."
                                                  "The output format should be mm/dd/yyyy."
                                                  "If No valid answer is found then return NA",
                                                  max_length = 60
                                                  )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class Initial_Rent_Commencement_Date (BaseModel):
    Initial_Rent_Commencement_Date : str = Field(description = "Extract the 'Initial Rent Commencement Date' from the lease document."
                                                 "This date should indicate when the tenant is first obligated to start paying rent, as specified in the lease."
                                                 "If the document ties the rent commencement to a particular event, such as the lease commencement, possession, or completion of improvements, capture these conditions."
                                                 "If no specific date is stated, note the relevant conditions that determine when rent payments begin."
                                                 "The output format should be mm/dd/yyyy.",
                                                 max_length = 60
                                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class How_Was_Rent_Commencement_Date_Determined (BaseModel):
    How_Was_Rent_Commencement_Date_Determined : str = Field(description = "Extract and explain how the 'Rent Commencement Date' was determined as described in the lease document."
                                                            "Identify any specific events or conditions that trigger the rent commencement, such as the delivery of possession, completion of tenant improvements, or a fixed date after lease commencement."
                                                            "If the lease provides any formulas, timelines, or other criteria for determining the rent commencement, summarize these details."
                                                            "If No valid answer is found then return NA",
                                                            max_length = 5000
                                                            )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Does_Rev_Share_Apply (BaseModel):
    Does_Rev_Share_Apply : str = Field(description = "Determine if a 'Revenue Share' provision applies specifically in relation to the sublease of the space."
                                       "Identify any clauses that require the tenant to share a portion of sublease income or profits with the landlord."
                                       "If applicable, outline the percentage or amount, any conditions for revenue sharing, and the method of calculation."
                                       "If no revenue share for subleasing is mentioned, indicate this clearly.",
                                       max_length = 5000
                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Monthly_Initial_Rent_at_Lease_Inception (BaseModel):
    Monthly_Initial_Rent_at_Lease_Inception : str = Field(description = "Extract the 'Monthly Initial Rent at Lease Inception' from the lease document."
                                                          "This should reflect the amount of rent payable on a monthly basis as specified at the start of the lease term."
                                                          "If the rent is expressed differently as annually or quarterly, convert it to a monthly figure and indicate how this conversion was performed."
                                                          "If No valid answer is found then return NA",
                                                          max_length = 5000
                                                          )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Monthly_Base_Rent_at_Closing (BaseModel):
    Monthly_Base_Rent_at_Closing : str = Field(description = "Extract the 'Monthly Base Rent at Closing' from the lease document."
                                               "This should reflect the rent amount that will be due monthly on that date."
                                               "Ensure to identify the currency and any conditions that may affect the base rent, such as any adjustments, escalations, or applicable concessions that may be in effect by the closing date."
                                               "If the rent is provided in a different format as annually or quarterly, convert it to a monthly amount and specify the conversion method used."
                                               "If No valid answer is found then return NA",
                                               max_length = 5000
                                               )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Escalation_Frequency_in_months (BaseModel):
    Escalation_Frequency_in_months : str = Field(description  = "Extract the 'Escalation Frequency' for rent payments from the lease document, specifically identifying how often rent increases occur, expressed in months."
                                                 "Look for any clauses that define the timing of these escalations, such as annual increases or other specific intervals."
                                                 "If the escalation is based on conditions or tied to specific events, summarize these as well."
                                                 "If no escalation frequency is stated, note this clearly.",
                                                 max_length = 5000
                                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    



class Escalation_Type_at_Closing (BaseModel) :
    Escalation_Type_at_Closing : str = Field(description = "Identify and extract the 'Escalation Type at Closing' from the lease document, focusing on the method used to increase rent as of the closing date."
                                             "Look for references to fixed percentage increases, CPI (Consumer Price Index) adjustments, step increases, or any other method specified in the lease."
                                             "Include details about how the escalation is calculated, including any applicable rates, formulas, or conditions."
                                             "If no escalation type is mentioned, note this clearly.",
                                             max_length = 5000
                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Escalation_Amount (BaseModel):
    Escalation_Amount : str = Field(description = "Extract the 'Escalation Amount' from the lease document, detailing the specific increase in rent at each escalation point."
                                    "Look for any fixed dollar amounts, percentage increases, or adjustments tied to external factors (e.g., CPI or market rates)."
                                    "Specify how the escalation amount is applied, whether as a flat increase or a percentage of the current rent."
                                    "If the escalation is tied to a formula or other variable, summarize the calculation method."
                                    "If no escalation amount is provided, note this clearly.",
                                    max_length = 5000
                                    )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payment_Frequency (BaseModel):
    Payment_Frequency : str = Field(description = "Extract the 'Payment Frequency' from the lease document, indicating how often rent payments are due as monthly, quarterly, annually."
                                    "Look for any clauses that specify the timing of payments, including any variations or special conditions that might affect the frequency as advance payments or deferred payment schedules."
                                    "If no payment frequency is explicitly mentioned, note any relevant conditions or references to standard payment terms.",
                                    max_length = 5000 
                                    )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Initial_Term_in_Months (BaseModel):
    Initial_Term_in_Months : str = Field(description = "Extract the 'Initial Term' of the lease, expressed in months, from the lease document."
                                         "Identify the total duration of the lease term as initially agreed upon, starting from the lease commencement date."
                                         "If the term is provided in years, convert it to months."
                                         "If there are any options for extension or early termination that impact the initial term, note them separately."
                                         "If No valid answer is found then return NA",
                                         max_length = 5000
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Current_Term_End_Date (BaseModel):
    Current_Term_End_Date : str = Field(description = "Extract the 'Current Term End Date' from the lease document."
                                        "This should indicate the final date of the current lease term, including any amendments, extensions, or renewals that are in effect."
                                        "If there are options for further renewal or extension beyond this date, note those separately."
                                        "If the end date is tied to specific conditions, such as a notice period or an event, summarize these details.",
                                        max_length = 500
                                        )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Final_Term_End_Date (BaseModel):
    Final_Term_End_Date : str = Field(description = "Extract the 'Final Term End Date,' including all potential or exercised renewal options, from the lease document."
                                      "This should reflect the absolute latest date the lease could terminate if all renewal or extension options are fully exercised."
                                      "Identify any automatic renewal provisions or conditions for exercising renewals, and if there are no renewals available, note the end date of the original term."
                                      "If No valid answer is found then return NA",
                                      max_length = 500
                                      )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class No_of_Renewals (BaseModel):
    No_of_Renewals : str = Field(description = "Extract the total number of renewal options available in the lease."
                                 "Identify how many times the tenant has the right to renew or extend the lease term, including any conditions or requirements for exercising these renewal options."
                                 "If the lease does not specify any renewals, or if renewals are not available, indicate this clearly.",
                                 max_length = 500
                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Renewal_Term_Length_in_months (BaseModel) :
    Renewal_Term_Length_in_months : str = Field(description = "Extract the length of each 'Renewal Term,' expressed in months, from the lease document."
                                                "Identify the duration of each renewal period that the tenant may exercise, and if the term is stated in years, convert it to months."
                                                "Note any variations in the length of different renewal terms, if applicable."
                                                "If no renewal terms are provided, indicate this clearly.",
                                                max_length = 5000
                                                )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Additional_Number_of_Renewals (BaseModel):
    Additional_Number_of_Renewals : str = Field(description = "Extract the 'Additional Number of Renewals' available beyond the initial renewal options, if any, from the lease document."
                                                "Identify any clauses that provide the tenant with the right to further extend the lease term after the original set of renewal options has been exhausted."
                                                "Include any conditions or requirements for exercising these additional renewals."
                                                "If no additional renewals are available, indicate this clearly.",
                                                max_length = 5000
                                                )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Additional_Renewal_Term_Length_in_months (BaseModel):
    Additional_Renewal_Term_Length_in_months : str = Field(description = "Extract the length of any 'Additional Renewal Terms' available, expressed in months, from the lease document."
                                                           "Identify the duration for each additional renewal period that the tenant may exercise after the initial renewal options."
                                                           "If the term is stated in years, convert it to months."
                                                           "If no additional renewal terms are specified, indicate this clearly.",
                                                           max_length = 5000
                                                           )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
 


class Payee_First_Name (BaseModel):
    Payee_First_Name : str = Field(description = "Extract the 'Payee First Name' from the lease document."
                                   "Identify the first name of the individual or entity designated as the payee for any financial transactions related to the lease."
                                   "If the payee is represented as a company or organization, look for the contact person’s first name associated with the payment."
                                   "If no payee first name is specified, indicate this clearly.",
                                   max_length = 500
                                   )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_Middle_Name (BaseModel):
    Payee_Middle_Name : str = Field(description = "Extract the 'Payee Middle Name' from the lease document."
                                    "Identify the middle name of the individual designated as the payee for any financial transactions related to the lease."
                                    "If the payee is a company or organization, check for any middle name associated with the contact person responsible for payments."
                                    "If no payee middle name is specified, indicate this clearly.",
                                    max_length = 500
                                    )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_Last_Name (BaseModel):
    Payee_Last_Name : str = Field(description = "Extract the 'Payee Last Name' from the lease document."
                                  "Identify the last name of the individual or entity designated as the payee for any financial transactions related to the lease."
                                  "If the payee is represented as a company or organization, look for the last name associated with the contact person responsible for payments."
                                  "If no payee last name is specified, indicate this clearly.",
                                  max_length = 500
                                  )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_Business_Name (BaseModel):
    Payee_Business_Name : str = Field(description = "Extract the 'Payee Business Name' from the lease document."
                                      "Identify the name of the business or entity designated as the payee for any financial transactions related to the lease."
                                      "If the payee is an individual, note any associated business name under which they operate."
                                      "If no payee business name is specified, indicate this clearly.",
                                      max_length = 500
                                      )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    



class Payee_Address_Line1 (BaseModel):
    Payee_Address_Line1 : str = Field(description = "Extract the 'Payee Address Line 1' from the lease document."
                                      "Identify the first line of the address for the individual or entity designated as the payee for financial transactions related to the lease."
                                      "This should include street address, building number, or any other relevant information."
                                      "If no address line 1 is specified, indicate this clearly.",
                                      max_length = 1000
                                      )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_Address_Line2 (BaseModel):
    Payee_Address_Line2 : str = Field(description = "Extract the 'Payee Address Line 2' from the lease document."
                                      "Identify the second line of the address for the individual or entity designated as the payee for financial transactions related to the lease."
                                      "This may include additional address details such as apartment numbers, suite numbers, or other relevant information that complements the first address line."
                                      "If no address line 2 is specified, indicate this clearly.",
                                      max_length = 1000
                                      )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_City (BaseModel):
    Payee_City :  str = Field(description = "Extract the 'Payee City' from the lease document."
                              "Identify the city associated with the individual or entity designated as the payee for any financial transactions related to the lease."
                              "If the city is not specified or is part of a larger address, indicate this clearly.",
                              max_length = 100
                              )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_State_or_Province (BaseModel):
    Payee_State_or_Province : str = Field(description = "Extract the 'Payee State/Province' from the lease document."
                                          "Identify the state or province of the individual or entity designated as the payee for any financial transactions related to the lease."
                                          "Ensure to capture the correct region associated with the payee's address."
                                          "If no state or province is specified, note this clearly.",
                                          max_length = 100
                                          )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class  Payee_PostalCode (BaseModel):
    Payee_PostalCode : str = Field(description = "Extract the 'Payee Postal Code' from the lease document."
                                   "Identify the postal or ZIP code associated with the individual or entity designated as the payee for financial transactions related to the lease."
                                   "Ensure to capture the correct postal code corresponding to the payee’s address."
                                   "If no postal code is specified, indicate this clearly.",
                                   max_length = 100
                                   )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Payee_phone (BaseModel):
    Payee_phone : str = Field(description = "Extract the 'Payee Phone Number' from the lease document."
                              "Identify the phone number provided for the individual or entity designated as the payee for any financial transactions related to the lease."
                              "Ensure to capture any area code or extensions mentioned."
                              "If no phone number is specified, note this clearly.",
                              max_length = 20
                              )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_mobile (BaseModel):
    Payee_mobile : str = Field(description = "Extract the 'Payee Mobile Number' from the lease document."
                               "Identify the mobile number provided for the individual or entity designated as the payee for any financial transactions related to the lease."
                               "Include any country or area codes."
                               "If no mobile number is specified, indicate this clearly.",
                               max_length = 20
                               )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Payee_email (BaseModel):
    Payee_email : str = Field(description = "Extract the 'Payee Email Address' from the lease document."
                              "Identify the email address provided for the individual or entity designated as the payee for any financial transactions related to the lease."
                              "Ensure to capture the full email address."
                              "If no email address is specified, indicate this clearly.",
                              max_length = 200
                              )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Aggregator_Name (BaseModel):
    Aggregator_Name : str = Field(description = "Extract the 'Aggregator Name' from the lease document."
                                  "Identify the name of the individual or entity responsible for aggregating or managing the lease-related payments, collections, or data."
                                  "If no aggregator is specified, indicate this clearly.",
                                  max_length = 200
                                  )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_First_Name (BaseModel):
    Landlord_First_Name : str = Field (description = "Extract the 'Landlord First Name' from the lease document."
                                       "Identify the first name of the individual or entity designated as the landlord or lessor in the lease."
                                       "If the landlord is an organization or business, note the contact person’s first name, if provided."
                                       "If no first name is specified, indicate this clearly.",
                                       max_length = 200
                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Middle_Name (BaseModel):
    Landlord_Middle_Name : str = Field(description = "Extract the 'Landlord Middle Name' from the lease document."
                                       "Identify the middle name of the individual designated as the landlord or lessor."
                                       "If no middle name is specified or if the landlord is an entity without individual names, indicate this clearly.",
                                       max_length = 200
                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Last_Name (BaseModel):
    Landlord_Last_Name : str = Field(description = "Extract the 'Landlord Last Name' from the lease document."
                                     "Identify the last name of the individual designated as the landlord or lessor."
                                     "If the landlord is an organization or entity, check for any individual contact person’s last name, if applicable."
                                     "If no last name is specified, indicate this clearly.",
                                     max_length = 200
                                     )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Business_Name (BaseModel):
    Landlord_Business_Name : str = Field(description = "Extract the 'Landlord Business Name' from the lease document."
                                         "Identify the name of the business or entity designated as the landlord or lessor in the lease."
                                         "If the landlord is an individual, note any associated business name under which they operate."
                                         "If no landlord business name is specified, indicate this clearly.",
                                         max_length = 200
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Address_Line1 (BaseModel):
    Landlord_Address_Line1 : str = Field(description = "Extract the 'Landlord Address Line 1' from the lease document."
                                         "Identify the first line of the address for the individual or entity designated as the landlord or lessor."
                                         "This should include the street address, building number, or any other relevant information."
                                         "If no address line 1 is specified, indicate this clearly.",
                                         max_length = 500
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Address_Line2 (BaseModel):
    Landlord_Address_Line2 : str = Field(description = "Extract the 'Landlord Address Line 2' from the lease document."
                                         "Identify the second line of the address for the individual or entity designated as the landlord or lessor."
                                         "This may include additional address details such as apartment numbers, suite numbers, or other relevant information that complements the first address line."
                                         "If no address line 2 is specified, indicate this clearly.",
                                         max_length = 500
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_City (BaseModel):
    Landlord_City : str = Field(description = "Extract the 'Landlord City' from the lease document."
                                "Identify the city associated with the individual or entity designated as the landlord or lessor."
                                "Ensure that the city matches the address provided for the landlord."
                                "If no city is specified, indicate this clearly.",
                                max_length = 200
                                )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_State_or_Province (BaseModel):
    Landlord_State_or_Province : str = Field(description = "Extract the 'Landlord State/Province' from the lease document."
                                             "Identify the state or province associated with the individual or entity designated as the landlord or lessor."
                                             "Ensure to capture the full state or province name as part of the landlord’s address."
                                             "If no state or province is specified, indicate this clearly.",
                                             max_length = 200
                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_Postal_Code (BaseModel):
    Landlord_Postal_Code : str = Field(description = "Extract the 'Landlord Postal Code' from the lease document."
                                       "Identify the postal or ZIP code associated with the individual or entity designated as the landlord or lessor."
                                       "Ensure the postal code is captured correctly as part of the landlord’s address."
                                       "If no postal code is specified, indicate this clearly.",
                                       max_length = 50
                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
    
class Landlord_phone (BaseModel):
    Landlord_phone : str = Field(description = "Extract the 'Landlord Phone Number' from the lease document."
                                 "Identify the phone number provided for the individual or entity designated as the landlord or lessor."
                                 "Ensure to capture any area codes or extensions mentioned."
                                 "If no phone number is specified, indicate this clearly.",
                                 max_length = 50
                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class Landlord_mobile (BaseModel):
    Landlord_mobile : str = Field(description = "Extract the 'Landlord Mobile Number' from the lease document."
                                  "Identify the mobile number provided for the individual or entity designated as the landlord or lessor."
                                  "Ensure to capture any country or area codes, if provided."
                                  "If no mobile number is specified, indicate this clearly.",
                                  max_length = 50
                                  )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Landlord_email (BaseModel):
    Landlord_email : str = Field(description = "Extract the 'Landlord Email Address' from the lease document."
                                 "Identify the email address provided for the individual or entity designated as the landlord or lessor."
                                 "Ensure to capture the full email address."
                                 "If no email address is specified, indicate this clearly.",
                                 max_length = 200
                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class No_of_Days_For_Notice (BaseModel):
    no_of_Days_For_Notice : str = Field(description = "Extract the 'no of Days for Notice for Renewal Option' from the lease document."
                                        "Identify the number of days the tenant or landlord is required to give notice prior to exercising the renewal option."
                                        "If the number of days is not specified, indicate this clearly.",
                                        max_length = 50
                                        )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Renewal_Notice_Comment (BaseModel):
    Renewal_Notice_Comment : str = Field(description = "Extract any 'Renewal Notice Comment' from the lease document."
                                         "Identify any additional details, conditions, or special instructions related to the renewal notice, such as format requirements, specific parties to be notified, or any other relevant provisions."
                                         "If no comment or additional information is provided, indicate this clearly.",
                                         max_length = 5000
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class VB_Required_to_Carry_Insurance (BaseModel):
    VB_Required_to_Carry_Insurance : str = Field(description = "Extract the 'VB Insurance Paragraph' from the lease document."
                                                 "Identify and capture the specific section or paragraph that details the insurance requirements for the tenant (VB)."
                                                 "This should include all relevant terms, conditions, coverage types, and obligations related to insurance."
                                                 "If no specific insurance paragraph is provided, indicate this clearly.",
                                                 max_length = 5000
                                                 )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class VB_Insurance_Paragraph (BaseModel):
    VB_Insurance_Paragraph : str = Field(description = "Extract the 'VB Insurance Paragraph' from the lease document."
                                         "Identify and capture the specific section or paragraph that details the insurance requirements for the tenant (VB)."
                                         "This should include all relevant terms, conditions, coverage types, and obligations related to insurance."
                                         "If no specific insurance paragraph is provided, indicate this clearly.",
                                         max_length = 5000
                                         )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")

class Is_VB_Required_to_Remove_Assets_at_of_Term (BaseModel):
    Is_VB_Required_to_Remove_Assets_at_of_Term : str = Field(description = "Extract the information regarding whether tenant (VB) is required to remove assets at the end of the lease term from the lease document."
                                                             "Identify any clauses or provisions that specify the tenant's obligations regarding the removal of personal property, fixtures, or improvements at lease termination."
                                                             "If there are no such requirements stated, indicate this clearly.",
                                                             max_length = 5000
                                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Tower_Revert_to_LL_Paragraph (BaseModel):
    Tower_Revert_to_LL_Paragraph : str = Field(description = "Extract the 'Tower Revert to Landlord Paragraph' from the lease document."
                                               "Identify and capture the specific section or paragraph that outlines the conditions under which the tower or related improvements revert to the landlord (LL) at the end of the lease term."
                                               "This should include any relevant details regarding ownership, timing, and obligations of the tenant regarding the reversion."
                                               "If no specific paragraph addressing this is provided, indicate this clearly.",
                                               max_length = 5000
                                               )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
    
class Does_VB_need_consent_to_assign_language (BaseModel):
    Does_VB_need_consent_to_assign_language : str = Field(description = "Extract the section addressing whether 'VB' requires consent to assign the lease from the lease document."
                                                          "Identify any clauses that specify the conditions under which the tenant must seek landlord approval to assign their lease rights or obligations."
                                                          "This should include details on the consent process, any exceptions, or conditions for assignment."
                                                          "If no specific language regarding consent to assign is provided, indicate this clearly.",
                                                          max_length = 5000
                                                          )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Notice_of_Assignment_to_LL_Paragraph (BaseModel):
    Notice_of_Assignment_to_LL_Paragraph : str = Field(description = "Extract the paragraph number related to the 'Notice of Assignment to Landlord' from the lease document."
                                                       "Identify the specific section or paragraph that outlines the requirements for notifying the landlord (LL) about an assignment of the lease."
                                                       "This should include the details regarding the timing, format, and any necessary information to be included in the notice."
                                                       "If no specific paragraph is provided, indicate this clearly.",
                                                       max_length = 5000
                                                       )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Is_there_a_ROFR_or_Purchase_Option (BaseModel):
    Is_there_a_ROFR_or_Purchase_Option : str = Field(description = "Extract information regarding the existence of a 'Right of First Refusal (ROFR)' or 'Purchase Option' from the lease document."
                                                     "Identify any clauses that explicitly state whether such rights are granted to the tenant and outline the conditions or terms associated with these rights."
                                                     "If no ROFR or Purchase Option is mentioned, indicate this clearly.",
                                                     max_length = 5000
                                                     )
    

class Holdover_Rent_Increase_Percentage (BaseModel):
    Holdover_Rent_Increase_Percentage : str = Field (description = "Extract the 'Holdover Rent Increase Percentage' from the lease document."
                                                     "Identify the specific percentage by which the rent will increase if the tenant holds over beyond the lease term."
                                                     "This should include any relevant details regarding the calculation or application of this increase."
                                                     "If no percentage is specified, indicate this clearly.",
                                                     max_length = 5000
                                                     )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Is_Consent_Required_To_Sublease_Paragraph (BaseModel):
    Is_Consent_Required_To_Sublease_Paragraph : str = Field(description ="Extract the 'Consent Required to Sublease Paragraph' from the lease document."
                                                            "Identify the section that specifies whether the tenant must obtain the landlord's consent before subleasing the premises."
                                                            "Include any relevant conditions, exceptions, or procedures for obtaining consent."
                                                            "If no such paragraph is provided, indicate this clearly.",
                                                            max_length = 5000
                                                            )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Is_Notice_to_the_LL_Required_for_Subleasing_Paragraph (BaseModel):
    Is_Notice_to_the_LL_Required_for_Subleasing_Paragraph : str = Field(description = "Extract the 'Notice to Landlord Required for Subleasing Paragraph' from the lease document."
                                                                        "Identify the section that outlines whether the tenant is required to provide notice to the landlord before subleasing the premises."
                                                                        "Include any details on timing, format, and specific information required in the notice."
                                                                        "If no such paragraph is provided, indicate this clearly.",
                                                                        max_length = 5000
                                                                        )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Is_LL_Consent_Required_For_Tenant_Equipment_Modification_Paragraph (BaseModel):
    Is_LL_Consent_Required_For_Tenant_Equipment_Modification_Paragraph : str = Field(description = "Extract the 'Landlord Consent Required for Tenant Equipment Modification Paragraph' from the lease document."
                                                                                     "Identify the section that specifies whether the tenant must obtain the landlord’s consent before making modifications or alterations to equipment on the premises."
                                                                                     "Include any relevant conditions, exceptions, or procedures for obtaining consent."
                                                                                     "If no such paragraph is provided, indicate this clearly.",
                                                                                     max_length = 5000
                                                                                     )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    
class Is_LL_Consent_Required_For_Improvements_To_Premises_Paragraph (BaseModel):
    Is_LL_Consent_Required_For_Improvements_To_Premises_Paragraph : str = Field(description = "Extract the 'Landlord Consent Required for Improvements to Premises Paragraph' from the lease document."
                                                                                "Identify the section that outlines whether the tenant must obtain the landlord’s consent before making improvements, alterations, or modifications to the premises."
                                                                                "Include any conditions, exceptions, or procedures for obtaining consent."
                                                                                "If no such paragraph is provided, indicate this clearly.",
                                                                                max_length = 5000
                                                                                )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Notification_Required_For_Access_Paragraph (BaseModel):
    Notification_Required_For_Access_Paragraph : str = Field(description = "Extract the 'Notification Required for Access Paragraph' from the lease document."
                                                             "Identify the section that specifies whether the tenant or landlord must provide notice before accessing the premises, including any details on timing, format, and conditions for providing such notice."
                                                             "If no specific paragraph is provided, indicate this clearly.",
                                                             max_length = 5000
                                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    



class Additional_sublease_or_sublease_modification_or_action_fees_to_LL_Paragraph (BaseModel):
    Additional_sublease_or_sublease_modification_or_action_fees_to_LL_Paragraph : str = Field(description = "Extract the 'Additional Sublease, Sublease Modification, or Action Fees to Landlord Paragraph' from the lease document."
                                                                                              "Identify the section that specifies any additional fees or charges the tenant must pay to the landlord related to subleasing, modifying a sublease, or taking any related actions."
                                                                                              "Include details on the types of fees, amounts, and conditions under which they apply."
                                                                                              "If no such paragraph is provided, indicate this clearly.",
                                                                                              max_length = 5000
                                                                                              )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    



class Does_Landlord_Have_Ability_To_Terminate_WO_Cause_Paragraph (BaseModel):
    Does_Landlord_Have_Ability_To_Terminate_WO_Cause_Paragraph : str = Field(description = "Extract the 'Landlord Ability to Terminate Without Cause Paragraph' from the lease document."
                                                                             "Identify the section that outlines whether the landlord has the right to terminate the lease without cause."
                                                                             "Include any details on notice requirements, conditions, or exceptions related to such termination."
                                                                             "If no such paragraph is provided, indicate this clearly.",
                                                                             max_length = 5000
                                                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Does_Landlord_Have_Ability_to_Non_Renew_a_Term_Paragraph (BaseModel):
   Does_Landlord_Have_Ability_to_Non_Renew_a_Term_Paragraph : str =  Field(description = "Extract the 'Landlord Ability to Non-Renew a Term Paragraph' from the lease document."
                                                                           "Identify the section that specifies whether the landlord has the right to decline renewing the lease term."
                                                                           "Include any conditions, notice requirements, or procedures for non-renewal."
                                                                           "If no such paragraph is provided, indicate this clearly.",
                                                                           max_length = 5000
                                                                           )
   Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
   PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                               "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class VB_Has_the_Ability_to_Terminate_Paragraph (BaseModel) :
    VB_Has_the_Ability_to_Terminate_Paragraph : str = Field(description = "Extract the 'VB Has the Ability to Terminate Paragraph' from the lease document."
                                                            "Identify the section that outlines whether the tenant (VB) has the right to terminate the lease."
                                                            "Include any conditions, notice periods, and specific circumstances under which the tenant may exercise this right."
                                                            "If no such paragraph is provided, indicate this clearly.",
                                                            max_length = 5000
                                                            )
    
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                        "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Amendment_1_Effective_Date (BaseModel):
    Amendment_1_Effective_Date : str = Field(description = "Extract the 'Amendment 1 Effective Date' from the lease document."
                                             "Identify the date when the first amendment to the lease became effective."
                                             "Ensure the date is clearly stated and corresponds to Amendment 1."
                                             "If no such amendment is provided, indicate this clearly.",
                                             max_length = 5000
                                             )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    

class Amendment_1_Rent_Commencement_Date (BaseModel):
    Amendment_1_Rent_Commencement_Date : str = Field(description = "Extract the 'Amendment 1 Rent Commencement Date' from the lease document."
                                                     "Identify the date when the rent specified in Amendment 1 begins."
                                                     "Ensure that the date is clearly stated and pertains specifically to the terms outlined in Amendment 1."
                                                     "If no such date is provided, indicate this clearly.",
                                                     max_length = 5000
                                                     )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                            "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    


class Amendment_1_Rent_Difference_from_Current_Term_Rent (BaseModel):
    Amendment_1_Rent_Difference_from_Current_Term_Rent : str = Field(description = "Extract the 'Amendment 1 Rent Difference from Current Term Rent' from the lease document."
                                                                     "Identify the change in rent specified in Amendment 1 compared to the rent under the current term."
                                                                     "Provide the difference in value, percentage, or any specific adjustment mentioned."
                                                                     "If no rent difference is outlined, indicate this clearly.",
                                                                     max_length = 5000
                                                                     )
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                "Return the Page No as a int"
                                         "If page or answer is not available respond as 0.")
    




entity_class = [Landlord_Entity_Name,
                Execution_Date,
                Initial_Lease_Commencement_Date,
                Initial_Rent_Commencement_Date,
                How_Was_Rent_Commencement_Date_Determined,
                Does_Rev_Share_Apply,
                Monthly_Initial_Rent_at_Lease_Inception,
                Monthly_Base_Rent_at_Closing,
                Escalation_Frequency_in_months,
                Escalation_Type_at_Closing,
                Escalation_Amount,
                Payment_Frequency,
                Initial_Term_in_Months,
                Current_Term_End_Date,
                Final_Term_End_Date,
                No_of_Renewals,
                Renewal_Term_Length_in_months,
                Additional_Number_of_Renewals,
                Additional_Renewal_Term_Length_in_months,
                Payee_First_Name,
                Payee_Middle_Name,
                Payee_Last_Name,
                Payee_Business_Name,
                Payee_Address_Line1,
                Payee_Address_Line2,
                Payee_City,
                Payee_State_or_Province,
                Payee_PostalCode,
                Payee_phone,
                Payee_mobile,
                Payee_email,
                Aggregator_Name,
                Landlord_First_Name,
                Landlord_Middle_Name,
                Landlord_Last_Name,
                Landlord_Business_Name,
                Landlord_Address_Line1,
                Landlord_Address_Line2,
                Landlord_City,
                Landlord_State_or_Province,
                Landlord_Postal_Code,
                Landlord_phone,
                Landlord_mobile,
                Landlord_email,
                No_of_Days_For_Notice,
                Renewal_Notice_Comment,
                VB_Required_to_Carry_Insurance,
                VB_Insurance_Paragraph,
                Is_VB_Required_to_Remove_Assets_at_of_Term,
                Tower_Revert_to_LL_Paragraph,
                Does_VB_need_consent_to_assign_language,
                Notice_of_Assignment_to_LL_Paragraph,
                Is_there_a_ROFR_or_Purchase_Option,
                Holdover_Rent_Increase_Percentage,
                Is_Consent_Required_To_Sublease_Paragraph,
                Is_Notice_to_the_LL_Required_for_Subleasing_Paragraph,
                Is_LL_Consent_Required_For_Tenant_Equipment_Modification_Paragraph,
                Is_LL_Consent_Required_For_Improvements_To_Premises_Paragraph,
                Notification_Required_For_Access_Paragraph,
                Additional_sublease_or_sublease_modification_or_action_fees_to_LL_Paragraph,
                Does_Landlord_Have_Ability_To_Terminate_WO_Cause_Paragraph,
                Does_Landlord_Have_Ability_to_Non_Renew_a_Term_Paragraph,
                VB_Has_the_Ability_to_Terminate_Paragraph,
                Amendment_1_Effective_Date,
                Amendment_1_Rent_Commencement_Date,
                Amendment_1_Rent_Difference_from_Current_Term_Rent,
                           
    ]






















































































































































