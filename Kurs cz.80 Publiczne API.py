import requests
import json
"""
    API - Application Programming Interface
"""

r = requests.get("")

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    
