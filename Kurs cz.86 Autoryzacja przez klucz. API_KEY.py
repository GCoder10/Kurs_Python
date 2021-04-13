"""
    API_KEY - klucz, autoryzacja użytkownika, klucz otrzymany podczas np.
    logowania się do serwera. Backend zwróci wtedy token - api_key, może być
    ograniczony czasowo, może być wymagany w różnych zapytaniach get,post itp.
    Jeżeli chcemy dostać się do zabezpieczonych miejsc w backend'zie
    poprzez jego routing. (chcemy dostać się do któregoś z zabezpieczonych
    endpointów, wymagających autoryzacji).
"""
'''
    Calendar Index:
        https://calendarific.com/

    Sign Up
    Login

    Tam bardziej został opisany po prostu token, natomiast API_KEY to
    otrzymywany string z ciągiem znaków potwierdzających naszą tożsamość
    po zarejestrowaniu się do danego API, można tak korzystać z wielu
    serwisów, np. Facebook itp. lub stworzyć własny np. w .NET
    .NET też do nadawania tokenów, potwierdzających tożsamość do miejsc,
    gdzie użytkownik musi być zarejestrowany i zalogowany.

    Po rejestracji może być ustalony jakiś limit requestów, np. 1000 na
    miesiąc.
    Dodatkowo jedno zapytanie na np. sekundę.
'''
"""
    https://calendarific.com/api-documentation

    Base URL
    Wykonanie Auth
    API_KEY przekazywane w parametrze zapytania, tak samo jak przekazywanie
    tokenów do backendu.
    Parametry np. przekazywane do backendu w .NET to JSON, JSON zostanie dalej
    obsłużony w środowisku C# i odpowiednio zweryfikowany np. API_KEY lub
    token konkretnego użytkownika.

    Taki backend też może zwracać błędy, komunikaty o nich w JSON.
"""
'''
    https://calendarific.com/api-documentation --> Required API Parameters

    Święta w Polsce w roku 2019:
    Różne, nie tylko lokalne, religijne, narodowe.
       "country": "pl",
       "year": 2019

    Zwrócone dane to słownik, którego wartościami są kolejne słowniki:
    KLUCZ: wartość
    a następnie wartości tych słowników to lista, lista zawierająca wszystkie
    Święta w Polsce w roku 2019, każde zapisane jako oddzielny słownik z
    kluczami i wartościami na temat danego Święta.
'''
"""
    Święta w Polsce w roku 2019 w Grudniu:
       "country": "pl",
       "year": 2019,
       "month": 12
"""
'''
    https://calendarific.com/api-documentation
    --> Premium Holiday API Endpoint Parameters:
        - language - język zwracanych informacji na temat Świąt.
'''

import requests
import json
import webbrowser
from pprint import pprint

params = {
    
   "api_key": "bebfe6202b3fab6360380cb28632953d4a2fa21a",
   "country": "pl",
   "year": 2019,
   "month": 12
    
}

r = requests.get('https://calendarific.com/api/v2/holidays/', params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint(content)
    
