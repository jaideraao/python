import json
import requests

response = requests.get("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios")

data = response.json()

print(data)
