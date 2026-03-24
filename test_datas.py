import requests

url = "http://localhost:5678/webhook-test/07b2a003-9070-4713-a8dd-77f97f363760"

data = {
    "row_number": 2,
    "name": "Test Cafe",
    "phone": "9876543210",
    "action": "call"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)