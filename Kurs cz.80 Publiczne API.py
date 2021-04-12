import requests
import json
"""
    API - Application Programming Interface
    Inter - pomiędzy
    Face - twarz

    bankomat - interface - przyciski.
    Nie obchodzi, jak to działa, po prostu z tego korzystamy.

    Korzystami z API jakiejś popularnej strony np.

    Spis API:
    https://github.com/public-apis/public-apis

    Strony mają ustawione limity takich anonimowych requestów do siebie, różnie,
    czasami 100 na dzień, 500 na dzień itd.
    Chodzi o to, żeby nie przeciążyć pracy serwera specjalnie / przypadkiem.

    Zazwyczaj wiadomo o Stack Overflow a jest dużo stron autorstwa ludzi od
    SO:
    https://stackexchange.com/sites


    Działanie na takim publicznym API, requestowanie go w ramach swoich ćwiczeń
    lub bardziej konkretnych celach.
    Jak było wspominane wcześniej, twórcy tych stron odpowiednio zabezpieczą
    swoją stronę przed nadmiernym korzystaniem z niej ze strony swojego api.


    https://api.stackexchange.com/docs/questions


    Dane wymieniane z takiego API do naszego programu będą oczywiście przez
    JSON jako uniwersalny pośrednik wymiany danych pomiedzy np. skrajnie
    różnymi środowiskami programistycznymi.
"""
'''

'''

r = requests.get("")

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    
