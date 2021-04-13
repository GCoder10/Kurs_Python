
"""
    Korzystanie z API:
        https://alexwohlbruck.github.io/cat-facts/
    BASE URL - bazowy adres, od którego rozpoczyna się wszystko
    Endpoints - miejsca możliwe do zasięgnięcia po rozpoczęciu pracy z bazowym
    adresem URL.
    Taki endpoint może zawierać dalej kolejne endpointy lub też można dodać
    parametry do zapytania, aby uzyskać interesujące dane z endpoint:
        https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html
    Takie serwery mogą posiadać limity dziennych zapytań lub też mogą być one
    nawet płatne.
"""
'''
    5 losowych faktów o kotach:
        params = {
        
            "amount": 5
        
        }

        r = request.get('https://cat-fact.herokuapp.com/facts/random', params)
'''
"""
    from pprint import pprint
    Dzięki takiemu importowi przy pomocy from nie będzie trzeba pisać:
        pprint.pprint
    Tylko od razu bezpośrednio:
        pprint
"""
'''
    Wypisanie faktu o kocie, każdy kot z listy słowników content.
    Każdy fakt widnieje jako oddzielny słownik, wszystkie słowniki są zapisane
    w liście content, dostanie się do poszczególnego słownika przy pomocy
    for cat i następnie do klucza "text" - fakt o kocie.
        for cat in content:
            print(cat["text"])
'''
"""
    5 losowych faktów o psach:
        params = {
            
            "amount": 5,
            "animal_type": "dog"
            
        }

        r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)
"""
'''
    Z takich publicznych API można też pobrać zdjęcia np:
        https://github.com/public-apis/public-apis
        --> Animals
        --> RandomCat
'''
"""
    https://shibe.online/
""" 
import requests
import json
import webbrowser
from pprint import pprint

params = {
    
    "amount": 5,
    "animal_type": "dog"
    
}

r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint(content)
    print("====================")
    for cat in content:
        print(cat["text"])
