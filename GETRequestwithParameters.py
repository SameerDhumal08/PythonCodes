import requests

url = "https://example.com/tickets"

params = {
    "status": "open"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
