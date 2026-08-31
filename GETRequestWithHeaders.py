import requests

url = "https://example.com/api/tickets"

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
