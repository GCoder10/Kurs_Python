"""
    
"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")


try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko jest okej")
