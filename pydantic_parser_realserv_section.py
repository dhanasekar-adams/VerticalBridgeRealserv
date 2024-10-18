from pydantic import BaseModel,Field
from datetime import datetime


class Trade_Name(BaseModel):

    Trade_Name: str = Field(description="What is the Trade Name or DBA or Do Business As Name in this agreement?"
                                        "There will multiple sections present some might have the relavant details some might not,ignore the irrelavant sections."
                                        "Try to Extract from the Initial section or from the Basic lease information."
                                        "Do not consider Landlord or Tenant Name as Trade Name."
                                         "If relavant answer is not available respond as NA.",
                            )
                                       
    
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class Effective_Date(BaseModel): 

    Effective_Date: str = Field(description="What is the Lease Date or the Effective Date of this agreement?"
                                            "Format the date as dd/mm/yyyy"
                                            "If relavant answer is not available respond as NA."
                                            "Give the response in a proper JSON Format.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class Tenant_Name(BaseModel):

    Tenant_Name: str = Field(description="What is the Name of the Tenant in this agreement?"
                                         "If relavant answer is not available respond as NA."
                                         "Give the response in a proper JSON Format.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    

class Landlord_Name(BaseModel):

    Landlord_Name: str = Field(description="What is the Name of the Landlord in this agreement?"
                                           "If relavant answer is not available respond as NA."
                                           "Give the response in a proper JSON Format.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")



class PremisesAddress(BaseModel):
    zip_code: str = Field(description="Should contain the zip code alone.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    state: str = Field(description="Should contain the state name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    city: str = Field(description="Should hold the city name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    full_address: str = Field(description="Should hold the full address of the premises.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")


    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


   

class Premises_Address(BaseModel):
    
    Premises_Address: PremisesAddress = Field(description="Since there might be multiple addresses in the context "
                                                          "provided to you, first gather all addresses. Try to "
                                                          "understand for which property this lease agreement is made or in other words,the Premises. "
                                                          "Do not respond with any other address."
                                                          "Give the response in a proper JSON Format.")
    

class Area_of_Premises(BaseModel):

    Area_of_Premises: str = Field(description="What is the Area of Premises mentioned this agreement?"
                                              "Format the answer in Square Feet."
                                              "If relavant answer is not available respond as NA."
                                              "Give the response in a proper JSON Format.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")




class Commencement_Date(BaseModel):

    Commencement_Date: str = Field(description="What is the Commencement Date  of this agreement?"
                                             "Format the date as dd/mm/yyyy"
                                             "If relavant answer is not available respond as NA."
                                                "Give the response in a proper JSON Format.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class Expiration_Date(BaseModel):

    Expiration_Date: str = Field(description="What is the Expiration Date or the Termination Date of this agreement?"
                                            "If not given direct date try to calculate from the commencement date if possible"
                                            "Format the date as dd/mm/yyyy"
                                            "If relavant answer is not available respond as NA."
                                             "Give the response in a proper JSON Format.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class TenantNoticeAddress(BaseModel):
    zip_code: str = Field(description="Should contain the zip code alone.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    state: str = Field(description="Should contain the state name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    city: str = Field(description="Should hold the city name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    full_address: str = Field(description="Should hold the full address of the tenat.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Tenant_Notice_Address(BaseModel):

    Tenant_Notice_Address: TenantNoticeAddress = Field(description="Since there might be multiple addresses in the context "
                                                                            "provided to you. Try to understand for whom this lease agreement is being "
                                                                            "entered to or in other words,the tenant.Find the address"
                                                                            "to where the copy fo the notoice for tenant should be delivered or the tenant address."
                                                                            "Do not respond with any other address."
                                                                               "Give the response in a proper JSON Format.")


class TenantNoticeCopyToAddress(BaseModel):
    zip_code: str = Field(description="Should contain the zip code alone.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    state: str = Field(description="Should contain the state name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    city: str = Field(description="Should hold the city name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    full_address: str = Field(description="Should hold the full address of the tenat notice address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Tenant_Notice_Copy_To_Address(BaseModel):

    Tenant_Notice_Copy_To_Address: TenantNoticeCopyToAddress = Field(description="Since there might be multiple addresses in the context "
                                                                            "provided to you. Try to understand for whom this lease agreement is being "
                                                                            "entered to or in other words,the tenant.Find the address"
                                                                            "to where the copy fo the notoice for tenant should be delivered or the tenant address."
                                                                            "Do not respond with any other address."
                                                                             "Give the response in a proper JSON Format.")
    
    
    

class BillingAddress(BaseModel):
    zip_code: str = Field(description="Should contain the zip code alone.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    state: str = Field(description="Should contain the state name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    city: str = Field(description="Should hold the city name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    full_address: str = Field(description="Should hold the full address of the billing address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")



class Billing_Address(BaseModel):

    Billing_Address: BillingAddress = Field(description="Since there might be multiple addresses in the context "
                                                          "provided to you. Try to understand for whom this lease agreement is being "
                                                          "billied to.Find the address of the billing or the landlord address."
                                                          "Do not respond with any other address."
                                                            "Give the response in a proper JSON Format.")




class BaseRent(BaseModel):
    Start_Date: datetime = Field(description="The start date of the rent. If the year part isn't mentioned in the "
                                             "line item explicitly, pick up the year from the commencement date and use "
                                             "it instead.If relavant answer is not available reply with NA.")
    
    End_Date: datetime = Field(description="The End date of the rent. If the year part isn't mentioned in the "
                                             "line item explicitly, pick up the year from the expiration date and use "
                                             "it instead.If relavant answer is not available reply with NA.")

    Monthly_Rent : str = Field(description="The rent amount of the month.Format the amount with $.If relavant answer is not available reply with NA.")
    
    Annual_Rent : str = Field(description="The rent amount of the annual.Format the amount with $.If relavant answer is not available reply with NA.")

    Rent_per_Square_Foot : str = Field(description="The rent amount per square foot.Format the amount with $.If relavant answer is not available reply with NA.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Base_Rent(BaseModel):

    Base_Rent: list[BaseRent] = Field(description="This lease agreement might contains the base rent details."
                                                  "Collect the Base rent details by looking at the whole context."
                                                  "There might be more than one year of base rent details,make sure to collect every tear or rows of the base rent."
                                                  "Give the response in a proper JSON Format.")



class AdditionalRent(BaseModel):
    Start_Date: datetime = Field(description="The start date of the additional rent. If the year part isn't mentioned in the "
                                             "line item explicitly, pick up the year from the commencement date and use "
                                             "it instead.If relavant answer is not available reply with NA.")
    
    End_Date: datetime = Field(description="The End date of the rent. If the year part isn't mentioned in the "
                                             "line item explicitly, pick up the year from the expiration date and use "
                                             "it instead.If relavant answer is not available reply with NA.")

    Monthly_Rent : str = Field(description="The additional rent amount of the month.Format the amount with $.If relavant answer is not available reply with NA.")
    
    Annual_Rent : str = Field(description="The additional rent amount of the annual.Format the amount with $.If relavant answer is not available reply with NA.")

    Rent_per_Square_Foot : str = Field(description="The additional rent amount per square foot.Format the amount with $.If relavant answer is not available reply with NA.")


    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Additional_Rent(BaseModel):

    Additional_Rent: list[AdditionalRent] = Field(description="This lease agreement might contains additional rent details. "
                                                              "Collect the additional rent terms by looking at the whole context."
                                                              "There might be more than one list of additional rent details,make sure to collect every list or rows of the additional rent."
                                                              "Give the response in a proper JSON Format.")

    


class RenewalOption(BaseModel):
    
    NOTICE_PERIOD: str = Field(description="State the period during which Tenant must provide written notice to Landlord to exercise the option to extend the lease term."
                                           "If relavant answer is not available reply with NA.")
    
    TERM: str = Field(description="Specify the duration of the Option Term.If relavant answer is not available reply with NA.")
    
    BREAKPOINT: str = Field(description="Describe the Breakpoint for percentage rent, if applicable.If relavant answer is not available reply with NA.")
    
    RENTAL_RATE: str = Field(description="Summarize how the Base Rent will be determined during the Option Term.If relavant answer is not available reply with NA.")
    
    ANNUAL_RENT_INCREASES_DURING_OPTION_TERM : str = Field(description="Indicate how the rent will increase annually during the Option Term"
                                                                       "If relavant answer is not available reply with NA.")
    
    SALES_TEST : str = Field(description="State the condition related to Tenant's sales performance required to exercise the option"
                                         "If relavant answer is not available reply with NA.")
    
    CONDITIONS_FOR_EXERCISING_THE_OPTION : str = Field(description="Summarize any specific conditions or restrictions that must be met for the option to be valid"
                                                                   "If relavant answer is not available reply with NA.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

    

class Renewal_Option(BaseModel):

    Renewal_Option: RenewalOption = Field(description="This lease agreement might contains Renewal Option details. "
                                                      "Extract the terms related to the Renewal Option provided in the lease document"
                                                      "Give the response in a proper JSON Format.")

    


class ExpansionOption(BaseModel):
    EXPANSION_OPTION: str = Field(description="Specify if the lease includes an option for the tenant to expand the leased premises."
                                               "If relavant answer is not available reply with NA.")
    CONDITIONS_FOR_EXERCISE: str = Field(description="Detail any conditions that must be met for the tenant to exercise the Expansion Option."
                                                     "If relavant answer is not available reply with NA.")
    EXERCISE_PROCEDURE: str = Field(description="Describe the procedure for exercising the Expansion Option, including notice requirements and deadlines."
                                                "If relavant answer is not available reply with NA.")
    TERMS_OF_EXPANSION: str = Field(description="Outline the terms of the expansion, including any changes to rent, lease term, or other conditions."
                                                "If relavant answer is not available reply with NA.")
    SPACE_ALLOCATION : str = Field(description="Specify the additional space available for expansion and any conditions related to its availability."
                                                "If relavant answer is not available reply with NA.")
    COSTS_AND_EXPENSES : str = Field(description="Detail any costs or expenses associated with the expansion, such as build-out costs or increased operational expenses."
                                                 "If relavant answer is not available reply with NA.")
    RENT_ADJUSTMENT : str = Field(description="Describe how rent will be adjusted for the expanded premises."
                                                "If relavant answer is not available reply with NA.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

   

class Expansion_Option(BaseModel):

    Expansion_Option: ExpansionOption = Field(description="This lease agreement might contains Expansion Option details. "
                                                          "Extract the terms related to the Expansion Option provided in the lease document"
                                                          "Give the response in a proper JSON Format.")

    

    

class TerminationRight(BaseModel):
    NOTICE_PERIOD: str = Field(description="State the minimum notice period required for the Landlord to terminate the lease."
                                           "If relavant answer is not available reply with NA.")
    CONDITIONS_FOR_TERMINATION: str = Field(description="Describe any specific conditions or restrictions on when the termination notice can be given."
                                                        "If relavant answer is not available reply with NA.")
    TENANT_OBLIGATIONS: str = Field(description="Summarize the obligations of the Tenant upon receiving the Termination Notice."
                                                "If relavant answer is not available reply with NA.")
    CONSEQUENCES_OF_FAILURE_TO_VACATE: str = Field(description="Describe the consequences if Tenant fails to vacate the Premises by the Termination Date."
                                                               "If relavant answer is not available reply with NA.")
    COMPENSATION_TO_TENANT : str = Field(description="Indicate whether there is any compensation due to Tenant upon termination."
                                                     "If relavant answer is not available reply with NA.")
    TERMINATION_FEE : str = Field(description="Specify if there is any termination fee required from Tenant."
                                              "If relavant answer is not available reply with NA.")
    ONGOING_LIABILITY : str = Field(description="State any ongoing liability of the Tenant post-termination."
                                                "If relavant answer is not available reply with NA.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Termination_Right(BaseModel):

    Termination_Right: TerminationRight = Field(description="This lease agreement might contains Landlord's or Tenant’s right to terminate the lease details. "
                                                            "Extract the terms related to the Landlord's or Tenant’s right to terminate the lease provided in the lease document"
                                                            "Give the response in a proper JSON Format.")

    



class RIGHTOFFIRSTOFFER(BaseModel):
    RIGHT_OF_FIRST_OFFER: str = Field(description="Specify if the lease includes a Right of First Offer (ROFO) for the tenant."
                                                         "If relavant answer is not available reply with NA.")
    CONDITIONS_FOR_EXERCISE: str = Field(description="Detail any conditions that must be met for the tenant to exercise the ROFO."
                                                     "If relavant answer is not available reply with NA.")
    EXERCISE_PROCEDURE: str = Field(description="Describe the procedure for exercising the ROFO, including notice requirements and deadlines"
                                                "If relavant answer is not available reply with NA.")
    SPACE_DESCRIPTION: str = Field(description="Specify the space to which the ROFO applies, including location and size."
                                                "If relavant answer is not available reply with NA.")
    OFFER_TERMS : str = Field(description="Outline the terms under which the Landlord will offer the space to the Tenant, including any conditions and deadlines for the offer."
                                          "If relavant answer is not available reply with NA.")
    RENT_AND_LEASE_TERMS : str = Field(description="Detail how the rent and other lease terms for the additional space will be determined."
                                                    "If relavant answer is not available reply with NA.")
    WAIVER_OF_ROFO : str = Field(description="Specify conditions under which the ROFO may be waived or considered void."
                                             "If relavant answer is not available reply with NA.")
    OTHER_CONDITIONS : str = Field(description="Include any additional conditions or requirements related to the ROFO."
                                               "If relavant answer is not available reply with NA.")

    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class RIGHT_OF_FIRST_OFFER(BaseModel):

    RIGHT_OF_FIRST_OFFER: RIGHTOFFIRSTOFFER = Field(description="This lease agreement might contains Right of First Offer (ROFO) option details. "
                                                                 "Extract the terms related to the Right of First Offer (ROFO) option provided in the lease document"
                                                                "Give the response in a proper JSON Format.")

    



class MONETARYDEFAULT(BaseModel):
    CURE_PERIOD: str = Field(description="Specify the time period Tenant has to remedy a monetary default after receiving written notice from Landlord "
                                         "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class NONMONETARYDEFAULT(BaseModel):
    IMMEDIATE_JEOPARDY: str = Field(description="Specify the time period Tenant has to remedy failures that immediately jeopardize Landlord’s interest "
                                                "If relavant answer is not available reply with NA.")

    OTHER_DEFAULTS: str = Field(description="Specify the time period Tenant has to remedy other defaults after receiving written notice from Landlord"
                                            "and any additional time allowed if the failure cannot be reasonably remedied within that period "
                                            "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")



class Default_Clause(BaseModel):

    MONETARY_DEFAULT: MONETARYDEFAULT = Field(description="This lease agreement might contains Monentary Default clause details. "
                                                          "Extract the details regarding Tenant's default conditions, including non-monetary defaults and calculate the days for each."
                                                          "Give the response in a proper JSON Format.")

    NON_MONETARY_DEFAULT: NONMONETARYDEFAULT = Field(description="This lease agreement might contains Non Monentary Default clause details. "
                                                                  "Extract the details regarding Tenant's default conditions, including monetary and cure periods and calculate the days for each."
                                                                 "Give the response in a proper JSON Format.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

    




    
class LATECHARGES(BaseModel):
    BASE_RENT: str = Field(description="Specify the late charge amount for overdue Base Rent"
                                        "If relavant answer is not available reply with NA.")

    PERCENTAGE_OR_ADDITIONAL_RENT: str = Field(description="Specify the late charge amount for overdue Percentage Rent and Additional Rent"
                                                            "If relavant answer is not available reply with NA.")

    EXCEPTIONS: str = Field(description="Describe any exceptions to the late charge policy"
                                         "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class CUREPERIODSFORDEFAULTS(BaseModel):
    MONETARY_OBLIGATIONS: str = Field(description="Specify the cure period for defaulting on monetary obligations, including the notice period and the time allowed for cure "
                                                    "If relavant answer is not available reply with NA.")

    OTHER_OBLIGATIONS: str = Field(description="Specify the cure period for other types of defaults, including the time allowed for cure "
                                                 "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class INTERESTONOVERDUEPAYMENTS(BaseModel):
    INTEREST_RATE: str = Field(description="Detail the interest rate applied to unpaid amounts, including any reference to the prime interest rate charged by Wells Fargo Bank"
                                               "plus additional percentage points, and the maximum lawful rate"
                                               "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class RETURNEDCHECKFEE(BaseModel):
    FEE_AMOUNT: str = Field(description="Specify the fee for returned checks due to insufficient funds"
                                         "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Late_Charges(BaseModel):

    LATE_CHARGES: LATECHARGES = Field(description="This lease agreement might contains LATE CHARGES details. "
                                                  "Extract the lease section details regarding Tenant's obligations for late charges."
                                                  "Give the response in a proper JSON Format.")

    INTEREST_ON_OVERDUE_PAYMENTS: INTERESTONOVERDUEPAYMENTS = Field(description="This lease agreement might contains INTEREST ON OVERDUE PAYMENTS details. "
                                                                                  "Extract the lease section details regarding Tenant's obligations for interest on overdue payments."
                                                                                "Give the response in a proper JSON Format.")

    CURE_PERIODS_FOR_DEFAULTS: CUREPERIODSFORDEFAULTS = Field(description="This lease agreement might contains CURE PERIODS FOR DEFAULTS details. "
                                                                          "Extract the lease section details regarding Tenant's obligations for cure periods for defaults."
                                                                          "Give the response in a proper JSON Format.")

    RETURNED_CHECK_FEE: RETURNEDCHECKFEE = Field(description="This lease agreement might contains RETURNED CHECK FEE details. "
                                                              "Extract the lease section details regarding Tenant's obligations for fees for returned checks."
                                                            "Give the response in a proper JSON Format.")




class HoldoverRent(BaseModel):
    HOLDOVER_RENT: str = Field(description="Describe the tenancy type and holdover rent if tenant remains in possession of the premises"
                                           "including any multipliers or comparisons to current market rent"
                                            "If relavant answer is not available reply with NA.")

    DELAYED_RENT_INCREASE: str = Field(description="Specify if and when the holdover rent increase is delayed due to ongoing negotiations between the parties"
                                                    "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Holdover_Rent(BaseModel):

    Holdover_Rent: HoldoverRent = Field(description="This lease agreement might contains Holdover Rent details. "
                                                  "Extract the lease section details regarding Holdover Rent"
                                                    "Give the response in a proper JSON Format.")

    

class ContractionOption(BaseModel):
    
    CONTRACTION_OPTION: str = Field(description="Specify if the lease includes a Contraction Option allowing Tenant to reduce the leased space"
                                                         "If relavant answer is not available reply with NA.")
    CONTRACTION_PERIOD: str = Field(description="Detail the period or timeframe during which the Tenant can exercise the Contraction Option."
                                                     "If relavant answer is not available reply with NA.")
    NOTICE_REQUIREMENTS: str = Field(description="Describe the procedure and timeline for notifying the Landlord of the Tenant's intention to exercise the Contraction Option."
                                                "If relavant answer is not available reply with NA.")
    REDUCED_SPACE: str = Field(description="Specify the amount or portion of the space that Tenant intends to reduce."
                                                "If relavant answer is not available reply with NA.")
    RENT_ADJUSTMENT : str = Field(description="Detail how the rent will be adjusted following the contraction."
                                          "If relavant answer is not available reply with NA.")
    CONTRACTION_EFFECTIVE_DATE : str = Field(description="Indicate the date when the contraction will become effective."
                                                    "If relavant answer is not available reply with NA.")
    COSTS_AND_EXPENSES : str = Field(description="Outline any costs or expenses associated with the contraction, such as modification costs or fees"
                                             "If relavant answer is not available reply with NA.")
    CONDITION_OF_PREMISES : str = Field(description="Specify any requirements related to the condition of the Premises following the contraction"
                                               "If relavant answer is not available reply with NA.")
    AMENDMENT_TO_LEASE : str = Field(description="Describe the process for amending the lease agreement to reflect the contraction"
                                                    "If relavant answer is not available reply with NA.")
    WAIVER_OF_OPTION : str = Field(description="Specify conditions under which the Contraction Option may be waived or considered void"
                                             "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


    
class Contraction_Option(BaseModel):

    Contraction_Option: ContractionOption = Field(description="This lease agreement might contains Contraction Option details. "
                                                  "Extract the terms related to the Contraction Option provided in the lease document "
                                                  "Give the response in a proper JSON Format.")

    


class TenantsInsuranceClause(BaseModel):
    
    TYPES_LIMITS: str = Field(description="Types of insurance required and the corresponding limits."
                                                         "If relavant answer is not available reply with NA.")
    POLICY_FORM: str = Field(description="Describe the requirements for the insurance policy form, including the rating and qualifications of the insurance company."
                                                     "If relavant answer is not available reply with NA.")
    ADDITIONAL_INSUREDS: str = Field(description="Identify the additional insureds specified in the lease, and any exceptions."
                                                "If relavant answer is not available reply with NA.")
    SELF_INSURANCE: str = Field(description="State if self-insurance is permitted and any related conditions."
                                                "If relavant answer is not available reply with NA.")
    
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


    
class Tenants_Insurance_Clause(BaseModel):

    Tenants_Insurance_Clause: TenantsInsuranceClause = Field(description="This lease agreement might contain Tenants Insurance Clause details. "
                                                                         "Extract the lease section details regarding Tenant's Insurance obligations."
                                                                         "Give the response in a proper JSON Format.")




class AssignmentClause(BaseModel):
    
    NOTICE_LL_RESPONSE_PERIODS: str = Field(description="Notice and response periods required by the lease."
                                                         "If relavant answer is not available reply with NA.")
    Landlord_Consent_Required: str = Field(description="State whether any assignments are permitted without landlord approval along with the conditions for consent."
                                                     "If relavant answer is not available reply with NA.")
    RENTAL_ADJUSTMENT: str = Field(description="Describe any rental adjustments that apply in the event of an assignment or sublet."
                                                "If relavant answer is not available reply with NA.")
    LANDLORDS_OPTIONS: str = Field(description="Describe the Consent, denial, termination, recapture of premises."
                                                "If relavant answer is not available reply with NA.")
    ASSIGNMENT_FEE: str = Field(description="State any assignment fees or processing fees required."
                                                "If relavant answer is not available reply with NA.")
    PROFIT_SHARE: str = Field(description="State any profit share provided in lease for subletting the premises."
                                                "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    



    
class Assignment_Clause(BaseModel):

    Assignment_Clause: AssignmentClause = Field(description="This lease agreement might contain Assignment Clause details. "
                                                            "Extract the lease section details regarding Assignment and Subletting"
                                                            "Give the response in a proper JSON Format.")




class CotenancyClause(BaseModel):
    
    CO_TENANCY_CONDITION: str = Field(description="Summarize the type of Co-tenancy, Co-tenancy condition, including the Major Tenants and any Qualified Replacement requirements."
                                                         "If relavant answer is not available reply with NA.")
    REMEDIES_FOR_UNSATISFIED_CONDITION: str = Field(description="Describe the remedies available if the co-tenancy condition is unsatisfied."
                                                     "If relavant answer is not available reply with NA.")
    TERMINATION_RIGHTS: str = Field(description="State the tenant's rights to terminate the lease if the co-tenancy condition remains unsatisfied for a specified period."
                                                "If relavant answer is not available reply with NA.")
    CO_TENANCY_SUSPENSION: str = Field(description="Note any waivers or suspensions of co-tenancy rights, including the time period affected."
                                                "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")



    
class Co_tenancy_Clause(BaseModel):

    Co_tenancy_Clause: CotenancyClause = Field(description="This lease agreement might contain Co-tenancy Clause details. "
                                                          "Extract the lease section details regarding Co-Tenancy and type of co-tenancy."
                                                           "Give the response in a proper JSON Format.")





class CommonAreaExpenses(BaseModel):
    
    Prorata_Share_Method: str = Field(description="Describe how the Tenant's Proportionate Share is calculated, including any specific square footage details."
                                                         "If relavant answer is not available reply with NA.")
    Excluded_Area: str = Field(description="Identify any areas that are excluded from the calculation of Common Area Expenses and provide the rationale behind the exclusions."
                                                     "If relavant answer is not available reply with NA.")
    Inclusions: str = Field(description="List all items and services included in Common Area Expenses, referencing specific examples from the lease language."
                                                "If relavant answer is not available reply with NA.")
    Exclusions: str = Field(description="Specify the items and services excluded from Common Area Expenses, explaining any conditions or exceptions."
                                                "If relavant answer is not available reply with NA.")
    Administrative_Fee: str = Field(description="State the percentage of the administrative fee and detail what it applies to, highlighting any exclusions."
                                                         "If relavant answer is not available reply with NA.")
    Payments: str = Field(description="Outline the payment structure for Common Area Expenses, including the frequency and any reconciliation requirements."
                                                     "If relavant answer is not available reply with NA.")
    Management_Fee: str = Field(description="Mention the percentage of the management fee, if applicable, and describe how it is calculated."
                                                "If relavant answer is not available reply with NA.")
    Capital_Repairs: str = Field(description="Summarize the conditions under which capital repairs can be included in Common Area Expenses, including amortization details."
                                                "If relavant answer is not available reply with NA.")
    Reconciliation_Deadline: str = Field(description="Provide the deadline for the annual reconciliation of Common Area Expenses."
                                                         "If relavant answer is not available reply with NA.")
    Estimates: str = Field(description="Detail the initial estimated monthly Common Area Expenses and the basis for the calculation."
                                                     "If relavant answer is not available reply with NA.")
    CAP: str = Field(description="Explain any caps on increases in Common Area Expenses, noting any exceptions."
                                                "If relavant answer is not available reply with NA.")
    Base_Year: str = Field(description="State the base year used for calculating Operating Costs."
                                                "If relavant answer is not available reply with NA.")
    Gross_Up: str = Field(description="Describe the gross-up provision, including the percentage used."
                                                         "If relavant answer is not available reply with NA.")
    Audit: str = Field(description="Outline the tenant's rights regarding auditing the landlord's calculations of Common Area Expenses, including any conditions or limitations."
                                                     "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")




    
class Common_Area_Expenses(BaseModel):

    Common_Area_Expenses: CommonAreaExpenses = Field(description="This lease agreement might contain Common Area Expenses details. "
                                                          "Extract the lease section details regarding Lease abstraction language detailing Common Area Expenses"
                                                             "Give the response in a proper JSON Format.")



class LandlordNoticeAddress(BaseModel):
    zip_code: str = Field(description="Should contain the zip code alone.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    state: str = Field(description="Should contain the state name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    city: str = Field(description="Should hold the city name from the address.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    full_address: str = Field(description="Should hold the full address of the landlord.If relavant answer is not available reply with NA.Response in the mentioned json format do not give an summary of the given lease agreement.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Landlord_Notice_Address(BaseModel):

    Landlord_Notice_Address: LandlordNoticeAddress = Field(description="Since there might be multiple addresses in the context "
                                                                       "provided to you, first gather all addresses. Try to "
                                                                       "understand by whom this lease agreement is being "
                                                                       "addressed to or in other words,the Landlord.Find the address"
                                                                       "to where the notoice for Landlord should be delivered."
                                                                       "Do not respond with any other address."
                                                                       "Give the response in a proper JSON Format.")





class GuarantorSub(BaseModel):
    
    GUARANTOR: str = Field(description="Identify the original guarantor under the lease."
                                                         "If relavant answer is not available reply with NA.")
    LIMITATIONS_OF_LIABILITY: str = Field(description="Limitations of liability related to the number of months, threshold amount by the guarantor and the guarantee."
                                                     "If relavant answer is not available reply with NA.")
    SPECIAL_TERMS_CONDITIONS: str = Field(description="Special terms and conditions related to the guarantor and the guarantee."
                                                "If relavant answer is not available reply with NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")



    
class Guarantor(BaseModel):

    Guarantor: GuarantorSub = Field(description="This lease agreement might contains Guarantee of Lease details. "
                                                 "Extract the terms related to the Guarantee of Lease."
                                                "Give the response in a proper JSON Format.")







class SurrenderSub(BaseModel):
    SURRENDER_OF_PREMISES_CONDITION: str = Field(description = "Describe the condition in which the tenant must return the premises"
                                                 "upon lease termination, including cleanliness and repair obligations."
                                                 "If relavant answer is not available respond as NA.")
    DEMOLITION_AND_REMOVAL : str = Field(description = "Detail any requirements for the tenant to demolish or"
                                         "remove improvements made during the lease, including the landlord’s discretion in this matter."
                                         "If relavant answer is not available respond as NA.")
    LANDLORDs_OPTIONS: str = Field(description = "State any specific options available to the landlord regarding the condition or"
                                   "alterations of the premises upon surrender."
                                   "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

class Surrender(BaseModel):
    Surrender: SurrenderSub = Field(description ="This lease agreement might contains surrender of the premises details. "
                                    "Extract the lease section details regarding the tenant's obligations upon lease termination, focusing on the surrender of the premises."
                                    "Give the response in a proper JSON Format.")



class SecurityDeposit(BaseModel):
    SECURITY_DEPOSIT_AMOUNT: str = Field(description = "Specify the total amount of the Security Deposit required under the lease & amendments."
                                         "If relavant answer is not available respond as NA.")
    DEPOSIT_TYPE: str = Field(description ="Indicate the type of deposit"
                              "If relavant answer is not available respond as NA.")
    APPLICATION_OF_SECURITY_DEPOSIT: str = Field(description ="Describe the Landlord's rights to apply the Security Deposit in case of Tenant's default or breach of lease obligations."
                                                 "If relavant answer is not available respond as NA.")
    Interest_on_Deposit: str = Field(description = "Whether interest is earned on the deposit"
                                     "If relavant answer is not available respond as NA.")
    RETURN_OF_SECURITY_DEPOSIT: str = Field(description = "Outline the timeframe and conditions under which any unapplied balance of the Security Deposit will be returned to the Tenant or the Tenant's assignee."
                                            "If relavant answer is not available respond as NA.")
    CONDITIONS_FOR_REDUCTION: str = Field(description =  "Detail the conditions under which the Tenant may reduce the Security Deposit, including any requirements for no default and the timing of the reduction."
                                          "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
    
class Security_Deposit(BaseModel):
    Security_Deposit: SecurityDeposit = Field(description = "This lease agreement might contains Security Deposit details."
                                              "Extract the lease section details regarding the Security Deposit"
                                              "Give the response in a proper JSON Format.")



class ParkingSpace(BaseModel):
    RESERVED_PARKING_STALLS_AND_RATE: str = Field(description = "Extract the minimum and maximum number of reserved stalls allowed and the rate per parking pass per month. If lease provides based on ratio then capture the ratio of reserved parking stalls to leased square footage."
                                                  "If relavant answer is not available respond as NA.")
    UNRESERVED_PARKING_STALLS_AND_RATE: str = Field(description =  "Provide details on the minimum and maximum number of unreserved stalls allowed and the rate per parking pass per month. If lease provides based on ratio then capture the ratio of unreserved parking stalls to leased square footage"
                                                    "If relavant answer is not available respond as NA.")
    GRACE_PERIOD_AND_LATE_FEE: str = Field(description =  "State the grace period allowed for parking fee payment and the corresponding late fee."
                                           "If relavant answer is not available respond as NA.")
    SPECIAL_CONDITIONS: str = Field(description =  "Note any special conditions or requirements related to parking, such as restrictions on assignment or subletting of parking passes, or cooperation in transportation management programs."
                                    "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Parking_Space(BaseModel):
    Parking_Space: ParkingSpace = Field(description ="This lease agreement might contains Parking Space details."
                                        "Extract the parking regulations details from the lease."
                                        "Give the response in a proper JSON Format.")


class UtilitiesSub(BaseModel):
    HVAC_SERVICE_HOURS: str = Field(description = "" 
                                    "If relavant answer is not available respond as NA.")
    ADDITIONAL_SERVICES: str = Field(description =  
                                     "If relavant answer is not available respond as NA.")
    METERED_UTILITIES: str = Field(description = 
                                   "If relavant answer is not available respond as NA.")
    JANITORIAL_SERVICES: str = Field(description =  
                                     "If relavant answer is not available respond as NA.")
    SUPPLEMENTAL_AIR_CONDITIONING: str = Field(description =  
                                               "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")

    
class Utilities(BaseModel):
    Utilities: UtilitiesSub = Field(description ="This lease agreement might contains Utilities details."
                                    "Extract the utilities and services details from the lease."
                                    "Give the response in a proper JSON Format.")


class PermittedUse(BaseModel):
    TENANTS_CORE_USE: str = Field(description =  "Extract the core uses allowed by the lease, including specific items and categories."
                                  "If relavant answer is not available respond as NA.")
    TENANTS_ANCILLARY_USE: str = Field(description =  "Extract the ancillary uses allowed by the lease, including specific items and categories"
                                       "If relavant answer is not available respond as NA.")
    RESTRICTIONS_AND_CONDITIONS: str = Field(description = "Note any conditions related to changes in use, such as notification requirements, restrictions on trade names, or other limitations"
                                             "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Permitted_Use(BaseModel):
    Permitted_Use: PermittedUse = Field(description ="This lease agreement might contains Permitted Use details."
                                        "Extract the permitted use details from the lease document."
                                        "Give the response in a proper JSON Format.")

class RadiusRestriction(BaseModel):
    Radius_Distance: str = Field(description =  "Specify the radius distance within which Tenant is restricted from operating a similar business."
                                 "If relavant answer is not available respond as NA.")
    Restricted_Locations: str = Field(description =  "List any specific shopping centers or areas where the Tenant is restricted from opening a similar business"
                                      "If relavant answer is not available respond as NA.")
    Exceptions: str = Field(description =  "Note any exceptions to the radius restriction, such as existing stores or specific locations where the restriction does not apply"
                            "If relavant answer is not available respond as NA.")
    REMEDIES_FOR_UNSATISFIED_CONDITION: str = Field(description =  "Describe the remedies available if tenant violated the Radius restriction clause"
                                                    "If relavant answer is not available respond as NA.")
    TERMINATION_RIGHTS: str = Field(description = "State the Landlord's rights to terminate the lease if the radius restriction condition is violated for a specified period."
                                    "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Radius_Restriction(BaseModel):
    Radius_Restriction: RadiusRestriction = Field(description ="This lease agreement might contains Radius Restriction details."
                                                  "Extract the radius restriction details from the lease document."
                                                  "Give the response in a proper JSON Format.")


class SalesKirckOut(BaseModel):
    NOTICE_PERIOD: str = Field(description =  "Extract the period within which the notice must be given following the Sales Test Period."
                               "If relavant answer is not available respond as NA.")
    CRITERIA: str = Field(description =  "List the criteria that must be met by the tenant, including conditions related to default, gross sales threshold, and any radius restrictions"
                          "If relavant answer is not available respond as NA.")
    COMPENSATION_TO_TENANT_BY_LANDLORD: str = Field(description =  "Specify if there is any compensation due to the tenant from the landlord, or state 'None' if not applicable."
                                                    "If relavant answer is not available respond as NA.")
    COMPENSATION_TO_LANDLORD_BY_TENANT: str = Field(description =  "Specify if there is any compensation due to the tenant from the landlord, or state 'None' if not applicable."
                                                    "If relavant answer is not available respond as NA.")
    GO_DARK_OR_TERMINATE: str = Field(description =  "Indicate whether the tenant has the option to 'Go Dark' or must terminate the lease."
                                      "If relavant answer is not available respond as NA.")
    TERMINATION_FEE_PAID_BY_TENANT: str = Field(description =  "Detail the termination fee the tenant is required to pay, including any unamortized costs or allowances"
                                                "If relavant answer is not available respond as NA.")
    Sales_KirckOut_NOTES: str = Field(description =  "Include any additional notes or conditions, such as the waiver of termination rights, timing of the termination, and special conditions related to opening other businesses within the radius restriction"
                                      "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Sales_KirckOut(BaseModel):
    Sales_KirckOut: SalesKirckOut = Field(description ="This lease agreement might contains Sales KirckOut details."
                                          "Extract the Sales Kick Out details from the lease agreemen."
                                          "Give the response in a proper JSON Format.")


class SignageClause(BaseModel):
    FASCIA_SIGNAGE_PROGRAM: str = Field(description = "Extract the approval of Tenant's standard fascia sign program, including any references to attached exhibits and the conditions for banner signage for seasonal promotions."
                                            "If relavant answer is not available respond as NA.")
    LOBBY_AND_SUITE_SIGN: str = Field(description = "Extract the approval of Tenant's standard Suite sign program and Lobby sign, including any references to attached exhibits and the conditions for suite & lobby signage"
                                      "If relavant answer is not available respond as NA.")
    WINDOW_COVERING_PROGRAM: str = Field(description = "Describe the approval and conditions related to Tenant's window covering program, referring to any applicable exhibits"
                                         "If relavant answer is not available respond as NA.")
    SEASONAL_PROMOTION_BANNERS: str = Field(description = "Outline the Tenant's rights to hang banners for seasonal promotions, including compliance requirements, approval process, and duration limits"
                                            "If relavant answer is not available respond as NA.")
    CHANNEL_LETTER_SIGNS: str = Field(description = "Extract the Tenant's rights to erect multi-colored individual channel letter signs on the building façade, including size restrictions and any code compliance"
                                      "If relavant answer is not available respond as NA.")
    MONUMENT_SIGNAGE_RIGHTS: str = Field(description = "Provide details about the Tenant's rights to display its tradename on a monument sign, including any conditions for installation, maintenance, and removal of the sign panel."
                                         "If relavant answer is not available respond as NA.")
    PYLON_SIGNAGE_RIGHTS: str = Field(description = "Provide details about the Tenant's rights to display its trade name on a pylon sign, including any conditions for installation, maintenance, and removal of the sign panel"
                                      "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Signage_Clause(BaseModel):
    Signage_Clause: SignageClause = Field(description ="This lease agreement might contains Signage Clause details."
                                          "Extract the details related to signage rights as per the lease."
                                          "Give the response in a proper JSON Format.")

    
class EstoppelCertificate(BaseModel):
    CERTIFICATION_TIMELINE: str = Field(description =  "Extract the time frame within which the Tenant or Landlord must deliver the certification statement upon request"
                                        "If relavant answer is not available respond as NA.")
    CERTIFICATION_CONTENT: str = Field(description = "State the required contents of the certification, including confirmation of whether the lease is unmodified and in full force, details of any modifications, payment dates for rent and additional charges, and any known defaults"
                                       "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Estoppel_Certificate(BaseModel):
    Estoppel_Certificate: EstoppelCertificate = Field(description ="This lease agreement might contains Estoppel Certificate details."
                                                      "Extract the certification of lease terms details from the lease document."
                                                      "Give the response in a proper JSON Format.")

class SubordinationSNDA(BaseModel):
    SUBORDINATION_TO_MORTGAGE: str = Field(description =  "Extract whether the lease is subject to and subordinate to any existing or future mortgages or similar encumbrances, and under what conditions"
                                           "If relavant answer is not available respond as NA.")
    NON_DISTURBANCE_AGREEMENT: str = Field(description = "State the conditions under which the Tenant will be granted a non-disturbance agreement by the mortgage holder, ensuring undisturbed possession of the premises"
                                           "If relavant answer is not available respond as NA.")
    ATTORNMENT: str = Field(description = "Detail the Tenant's obligations to attorn to any subsequent purchaser or transferee of the Landlord's interest, including any conditions related to the new owner's assumption of Landlord's obligations"
                            "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Subordination_SNDA(BaseModel):
    Subordination_SNDA: SubordinationSNDA = Field(description ="This lease agreement might contains Subordination SNDA details."
                                                  "Extract the encumbrance and attornment details from the lease."
                                                  "Give the response in a proper JSON Format.")


class TenantImprovementAllowance(BaseModel):
    TENANT_IMPROVEMENT_ALLOWANCE: str = Field(description = "Extract the conditions under which the Tenant will be reimbursed for their improvement work, including any maximum per square foot reimbursement and specific exclusions from reimbursement" 
                                              "If relavant answer is not available respond as NA.")
    REPAYMENT_OBLIGATIONS: str = Field(description =  "Detail the Tenant's obligations to repay the unamortized portion of the Tenant Allowance if the lease is terminated early or upon any assignment."
                                       "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    

    
class Tenant_Improvement_Allowance(BaseModel):
    Tenant_Improvement_Allowance: TenantImprovementAllowance = Field(description ="This lease agreement might contains Tenant Improvement Allowance details."
                                                                     "Extract the Tenant Improvement Allowance (TIA) details from the lease."
                                                                     "Give the response in a proper JSON Format.")

    
class RelocationSub(BaseModel):
    RELOCATION_RIGHTS: str = Field(description = "Extract Landlord's right to relocate the Tenant, including the notice period required, conditions for the new space (such as location, size, and features), and any limits on rent and tenant's share."
                                   "If relavant answer is not available respond as NA.")
    REIMBURSEMENT_OF_COSTS: str = Field(description = "Detail the costs that the Landlord will cover related to the relocation, including relocation and reconnection of Tenant’s personal property and any other reasonable out-of-pocket costs."
                                        "If relavant answer is not available respond as NA.")
    TENANTS_OPTIONS: str = Field(description = "Explain the Tenant's options if the relocation space is not acceptable, including the notice period to terminate the lease and the conditions under which the lease will terminate"
                                 "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
class Relocation(BaseModel):
    Relocation: RelocationSub = Field(description ="This lease agreement might contains Relocation details."
                                      "Extract the tenant relocation terms from the lease."
                                      "Give the response in a proper JSON Format.")


class TenantsMaintenance(BaseModel):
    TENANTS_MAINTENANCE_OBLIGATIONS: str = Field(description = "the Tenant's responsibilities for maintaining and repairing the Premises, including any specific items or systems that the Tenant is responsible for, such as appliances, fixtures, and non-standard equipment"
                                                 "If relavant answer is not available respond as NA.")
    REIMBURSEMENT_OF_REPAIR_COSTS: str = Field(description = "Detail the conditions under which the Tenant must reimburse the Landlord for repairs, including any costs incurred by the Landlord on behalf of the Tenant and the process for reimbursement"
                                               "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Tenants_Maintenance(BaseModel):
    Tenants_Maintenance: TenantsMaintenance = Field(description ="This lease agreement might contains Tenants Maintenance details."
                                                    "Extract the tenant’s maintenance and repair obligations."
                                                    "Give the response in a proper JSON Format.")


class LandlordMaintenance(BaseModel):
    LANDLORDS_MAINTENANCE_AND_REPAIR_RESPONSIBILITIES: str = Field(description = "Extract the Landlord’s obligations for maintaining and repairing HVAC equipment (excluding supplemental equipment), Common Areas, roof, foundations, footings, exterior surfaces, and building systems. Note any exceptions as specified in the lease"
                                                                   "If relavant answer is not available respond as NA.")
    TENANTS_REPAIR_RESTRICTIONS: str = Field(description = "Detail any restrictions on the Tenant’s ability to make repairs at the Landlord’s expense or by rental offset, including any legal rights the Tenant is waiving"
                                             "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Landlord_Maintenance(BaseModel):
    Landlord_Maintenance: LandlordMaintenance = Field(description ="This lease agreement might contains Landlord Maintenance details."
                                                      "Extract the Landlord’s responsibilities for maintenance and repair."
                                                      "Give the response in a proper JSON Format.")


class AlterationsSub(BaseModel):
    COSMETIC_ALTERATIONS: str = Field(description = "Extract the conditions under which the Tenant may make cosmetic alterations without Landlord’s prior consent, including the cost limit and restrictions on affecting structural, electrical, or mechanical components"
                                      "If relavant answer is not available respond as NA.")
    ALTERATIONS_REQUIRING_LANDLORDS_CONSENT: str = Field(description = "Detail the requirements for Tenant to obtain Landlord’s consent for alterations that are not cosmetic, including any conditions under which Landlord’s consent may be unreasonably withheld, and any additional requirements imposed by Landlord"
                                                         "If relavant answer is not available respond as NA.")
    SUPERVISION_FEE: str = Field(description = "State the percentage fee that Landlord will charge for supervising the Alterations"
                                 "If relavant answer is not available respond as NA.")
    OWNERSHIP_AND_REMOVAL_OF_ALTERATIONS: str = Field(description = "Explain that all Alterations, except moveable trade fixtures and furniture, become Landlord’s property and must be surrendered with the Premises at the end of the Lease term. Include details on any required removals and the Tenant’s responsibilities for repairing damage and restoring the Premises"
                                                      "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
    
class Alterations(BaseModel):
    Alterations: AlterationsSub  = Field(description ="This lease agreement might contains Alterations details."
                                         "Extract the Tenant’s obligations and limitations regarding alterations to the Premises,"
                                         "Give the response in a proper JSON Format.")


class SatelliteDish(BaseModel):
    INSTALLATION_AND_MAINTENANCE: str = Field(description = "Summarize the Tenant’s right to install, maintain, and operate the Dish at Tenant's sole expense, including the method of installation and responsibilities for any damage caused."
                                              "If relavant answer is not available respond as NA.")
    Satellite_Dish_RELOCATION: str = Field(description = "Detail the conditions under which Landlord may request Tenant to relocate the Dish, including compliance with legal requirements or construction of additional improvements, and Tenant’s responsibility for costs and coordination of relocation"
                                           "If relavant answer is not available respond as NA.")
    REPAIRS_AND_REPLACEMENTS: str = Field(description = "Specify Tenant’s responsibilities for repairing any damage caused by the Dish, obtaining necessary licenses or approvals, and maintaining the Dish in good condition. Include Landlord’s right to remove the Dish if maintenance is inadequate and the conditions for removal and restoration of the Premises"
                                          "If relavant answer is not available respond as NA.")
    PROPERTY_AND_LIEN_ISSUES: str = Field(description = "Explain that the Dish remains Tenant’s property, not becoming a fixture, and Tenant’s obligation to remove the Dish and restore the Premises at the end of the Lease. Include Tenant’s indemnification obligations related to any claims, damages, or liens"
                                          "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")
    
class Satellite_Dish(BaseModel):
  Satellite_Dish: SatelliteDish  = Field(description ="This lease agreement might contains Satellite Dish details."
                                               "Extract the Tenant's rights and responsibilities related to the installation,"
                                           "maintenance, and operation of a roof-mounted satellite dish antenna (the 'Dish')."
                                           "Give the response in a proper JSON Format.")



class FlexFurniture(BaseModel):
    DELIVERY_AND_INSTALLATION: str = Field(description = "the Landlord will deliver and install certain items of Flex Furniture in the Premises as outlined in the Spec Package."
                                           "If relavant answer is not available respond as NA.")
    USE_AND_MAINTENANCE: str = Field(description = "Detail that the Tenant may use the Flex Furniture during the Term and must maintain it in the same condition as received, reasonable wear and tear excepted. Include Landlord's warranty of the Flex Furniture being new or in “like new” condition, and Tenant's obligations to notify Landlord and use Landlord-approved contractors for repairs or relocation"
                                     "If relavant answer is not available respond as NA.")
    OWNERSHIP_AND_EXTENSION_TERMS: str = Field(description = "Explain that if Tenant extends the Lease and the Basic Rent includes a component for the Flex Furniture, title to the Flex Furniture will be conveyed to Tenant upon expiration of the extension term. If the Lease is not extended, the Flex Furniture must be returned to Landlord in the required condition upon Lease expiration or earlier termination"
                                               "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Flex_Furniture(BaseModel):
  Flex_Furniture: FlexFurniture  = Field(description ="This lease agreement might contains Flex Furniture details."
                                               "Extract the terms related to the Flex Furniture provided by the Landlord."
                                           "Give the response in a proper JSON Format.")



class FitnessCenter(BaseModel):
    FITNESS_CENTER_ACCESS_AND_USE: str = Field(description = "Extrat Tenant’s employees must execute Landlord’s standard waiver of liability form and pay any applicable one-time or monthly fee to use the fitness center and shower facilities. Specify that access is granted to Tenant’s employees (Fitness Center Users) during the Term as long as Tenant is not in Default"
                                               "If relavant answer is not available respond as NA.")
    FITNESS_CENTER_COSTS_AND_EXPENSES: str = Field(description = "Indicate that no separate charges will be assessed to Fitness Center Users for use of the Fitness Center during the initial Term, except for any towel/laundry fees. State that the costs of operating, maintaining, and repairing the Fitness Center will be included as part of Operating Expenses."
                                    "If relavant answer is not available respond as NA.")
    FITNESS_CENTER_MODIFICATION_AND_LIABILITY: str = Field(description = "Explain that Landlord may expand, contract, eliminate, or modify the Fitness Center at Landlord’s discretion without affecting Tenant’s Basic Rent or constituting a default. State that Tenant waives any claims against Landlord for personal injury or property damage related to the Fitness Center use."
                                            "If relavant answer is not available respond as NA.")
    FITNESS_CENTER_TRANSFER_AND_ASSIGNMENT: str = Field(description = "Specify that Tenant’s right to use the Fitness Center is non-transferable and cannot be assigned without Landlord’s prior written consent"
                                         "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Fitness_Center(BaseModel):
  Fitness_Center: FitnessCenter  = Field(description ="This lease agreement might contains Fitness Center details."
                                               "Extract the terms related to the Fitness Center provided in the lease document."
                                           "Give the response in a proper JSON Format.")


class ConferenceCenter(BaseModel):
    CONFERENCE_CENTER_ACCESS_AND_USE: str = Field(description = "State that the Conference Center is available for use by Tenant subject to availability and Landlord’s procedures and charges. Access is granted on a reserved basis"
                                                  "If relavant answer is not available respond as NA.")
    CONFERENCE_CENTER_COSTS_AND_EXPENSES: str = Field(description = "Indicate that Tenant may be subject to Landlord’s charges for use of the Conference Center, if any, and that Tenant’s use is governed by Landlord’s reasonable rules and regulations"
                                    "If relavant answer is not available respond as NA.")
    CONFERENCE_CENTER_MODIFICATION_AND_LIABILITY: str = Field(description = "Explain that Landlord is not liable for the existence, condition, or availability of the Conference Center, nor is Landlord obligated to enforce or make reservations. Tenant waives any claims against Landlord related to the Conference Center. No changes or termination of the Conference Center will affect Tenant’s Rent or constitute a default"
                                            "If relavant answer is not available respond as NA.")
    CONFERENCE_CENTER_TRANSFER_AND_ASSIGNMENT: str = Field(description = "Specify that Tenant’s right to use the Conference Center is subject to Landlord’s procedures and is non-transferable without Landlord’s consent"
                                         "If relavant answer is not available respond as NA.")
    Position: list[str] = Field(description="Extract the heading or section Number under which the relevant information is taken for answer generation."
                                         "If multiple heading or section Number have the answer then give the earliest heading or section Number under which the answer is present as the answer."
                                       "If answer is scattered among the heading or section Number then list the unique heading or section Number in ascending order."
                                         "If heading or section Number or answer is not available respond as NA.")
    
    PageNum : list[int] = Field(description="The pages from which the answer is extracted."
                                         "If page or answer is not available respond as NA.")


class Conference_Center(BaseModel):
  Conference_Center: ConferenceCenter  = Field(description ="This lease agreement might contains Conference Center details."
                                                     "Extract the terms related to the Conference Center provided in the lease document."
                                                "Give the response in a proper JSON Format.")



entity_class = [Trade_Name,
                  Effective_Date,
                  Tenant_Name,
                  Landlord_Name,
                  Premises_Address,
                  Area_of_Premises,
                  Commencement_Date,
                  Expiration_Date,
                  Tenant_Notice_Address,
                  Tenant_Notice_Copy_To_Address,
                  Billing_Address,
                  Base_Rent,
                  Additional_Rent,
                  Renewal_Option,
                  Expansion_Option,
                  Termination_Right,
                  RIGHT_OF_FIRST_OFFER,
                  Default_Clause,
                  Late_Charges,
                  Holdover_Rent,
                  Contraction_Option,
                  Tenants_Insurance_Clause,
                  Assignment_Clause,
                  Co_tenancy_Clause,
                  Common_Area_Expenses,
                  Landlord_Notice_Address,
                  Guarantor,
                  Surrender,
                  Security_Deposit,
                  Parking_Space,
                  Utilities,
                  Permitted_Use,
                  Radius_Restriction,
                  Sales_KirckOut,
                  Signage_Clause,
                  Estoppel_Certificate,
                  Subordination_SNDA,
                  Tenant_Improvement_Allowance,
                  Relocation,
                  Tenants_Maintenance,
                  Landlord_Maintenance,
                  Alterations,
                  Satellite_Dish,
                  Flex_Furniture,
                  Fitness_Center,
                  Conference_Center
                  ]
