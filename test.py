import requests

BASE = "http://localhost:5000/"

response = requests.patch(BASE + "video/2", {"name": "ciao youtube", "likes":21})
print(response)

res=requests.get(BASE + "video/2")
print(res.json())