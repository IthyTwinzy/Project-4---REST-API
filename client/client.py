import requests
import json

BACKEND_URL: str = 'http://127.0.0.1:5000/'

response = requests.get(BACKEND_URL)
print(response.json())
data = json.loads(response.text)
#TEST
print(f"Webserver Message: {data.get('message')}")