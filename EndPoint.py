import requests
from requests.structures import CaseInsensitiveDict

url = "http://20.204.87.110/webhook"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = 'DETECTION JSON PAYLOAD'
resp = requests.post(url, headers=headers, data=str(data))
print(resp.status_code)
