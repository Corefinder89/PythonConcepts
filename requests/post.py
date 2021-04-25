import requests
import json

url = "https://reqres.in/api/users"

payload = {"name":"morpheus","job":"leader"}

headers = {'Content-Type': "application/json"}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

if response.status_code == 201:
    print(response.json())
else:
    print(response.status_code)
