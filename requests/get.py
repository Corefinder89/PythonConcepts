import requests

endpoint = "https://reqres.in/api/users"

querystring = {"page":"3"}

payload = ""

headers = {'Content-Type': "application/json"}

response = requests.request(
    "GET",
    endpoint,
    data=payload,
    headers=headers,
    params=querystring
)


if response.status_code == 200:
    # print(response.json())
    # print(response.json().get("data"))
    print(response.json().get("data"))
else:
    print(response.status_code)
