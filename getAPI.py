import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    for user in data:
        print("Name:", user["name"])
        print("Email:", user["email"])
else:
    print("Request failed")
