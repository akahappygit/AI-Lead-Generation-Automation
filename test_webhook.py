import requests

user_message = "Can you tell me about black hoels in 3 to 4 lines?"

request_message = {
    "message": user_message
}

url = "http://localhost:5678/webhook-test/0b600c30-285b-4fe8-838b-05a458e46774"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])