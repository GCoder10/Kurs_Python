"""
    Breed - rasa
    https://docs.thecatapi.com/example-by-breed
    
"""

import requests
import json
import webbrowser
from pprint import pprint

params = {
    
    
    
}

r = requests.get('', params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint(content)
    
