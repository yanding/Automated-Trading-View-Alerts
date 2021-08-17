import requests
from requests.structures import CaseInsensitiveDict

url = "http://20.204.87.110/webhook"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"key": "x", "message": "Negative Divergence Detected", "exchange": "BINANCE", "action": "SELL", "ticker": "ETHUSDTPERP", "volume": "12345.2", "price": "3167.8", "time": "UTC +530 TIME"}'
resp = requests.post(url, headers=headers, data=data)
print(resp.status_code)
