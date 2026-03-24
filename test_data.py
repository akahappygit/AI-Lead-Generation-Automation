import requests

url = "http://localhost:5678/webhook-test/10fe2a3c-cbef-4d0d-9c11-267a86269f53 "

data = {
    "row_number": 2,
    "name": "Test Cafe",
    "phone": "9876543210",
    "action": "call"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)