import requests

BASE = "http://localhost:5000/"

response = requests.put(BASE + "video/1", {"name":"nome1", "views":100, "likes":10})
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())
