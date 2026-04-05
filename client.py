import requests
import json
response = requests.get('http://127.0.0.1:5000/')
print(response.json())
data = json.loads(response.text)
#TEST
print(f"Webserver Message: {data.get('message')}")