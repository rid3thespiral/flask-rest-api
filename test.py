import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + "helloworld")
print(response.json())

response = requests.post(BASE + "helloworld")
print(response.json())