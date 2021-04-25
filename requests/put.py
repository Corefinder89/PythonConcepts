import requests
import json

url = "https://reqres.in/api/users/2"

payload = {"name":"morpheus","job":"zion resident"}
headers = {'Content-Type': "application/json"}

response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
