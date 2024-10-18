import requests

url = "http://127.0.0.1:9006/?folderName=sample&Id=101"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
#PeterbiltIllinoisVJ
#NEWPORT_COAST_NEWPORT BEAUTY SALON
#Concentric_SL6_FLA_Lease_2180PremierRow (Executed)
#converted_US-VA-8246_MLA_062101_VerizonWireless
#Editable_Lease Agreement.pdf (1)
