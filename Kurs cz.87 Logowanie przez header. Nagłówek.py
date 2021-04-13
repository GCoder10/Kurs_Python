"""
    https://docs.thecatapi.com/authentication
    --> Authentication --> Request Header

    Nagłówek jako najbardziej bezpieczna opcja przekazywania tak ważnych
    informacji do backendu jak api_key lub token.

    https://docs.thecatapi.com/favourites
    API Key Required
"""
"""
    https://thecatapi.com/signup
    Get API_KEY via email
    ID User

    Informacje przekazywane nagłówkiem nie są widoczne od razu, trzeba
    wejść do nagłówka.
"""
'''
    W zapytaniu trzeba przesłać zmienną nazwaną dla użycia nagłówka:
    headers = headers
    Interpreter - kompilator domyśli się, że po prawej stronie znaku
    równości to zmienna, tak samo jak kompilator np. w C++/C++11 domyśla się
    w przypadku polimorfizmu - przeciążania funkcji / procedur, z jakiej
    funkcji / procedury chcemy skorzystać w danej chwili według typu przekazywanych
    parametrów do takiej funkcji / procedury.
'''
"""
    Kurs_cz87_Credentials
    Data Credentials - Dane Uwierzytelniające

    Przekazanie informacji z innego pliku, przechowywanego tam nagłówka:
        headers = Kurs_cz87_Credentials.headers
"""

import requests
import json
import webbrowser
import Kurs_cz87_Credentials
from pprint import pprint

r = requests.get('https://api.thecatapi.com/v1/favourites/', headers = Kurs_cz87_Credentials.headers)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint(content)
    
