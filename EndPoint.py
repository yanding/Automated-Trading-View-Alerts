import requests
from requests.structures import CaseInsensitiveDict

url = "http://20.204.87.110/webhook"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"key": "x", "message": "Negative Divergence Detected", "exchange": {{exchange}}, "action": "buy", "ticker": {{ticker}}, "volume": {{volume}}, "price": {{open}}, "time": {{time}}}'
resp = requests.post(url, headers=headers, data=str(data))
print(resp.status_code)
