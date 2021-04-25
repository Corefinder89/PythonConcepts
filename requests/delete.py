import requests

url = "https://reqres.in/api/users/978" # endpoint

payload = ""
headers = {'Content-Type': "application/json"}

response = requests.request("DELETE", url, data=payload, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
