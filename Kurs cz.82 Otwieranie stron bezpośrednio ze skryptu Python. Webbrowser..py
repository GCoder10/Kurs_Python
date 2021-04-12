import requests
import json
import pprint
import webbrowser
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
    Używanie formatu JSON jako uniwersalny nośnik wymiany danych pomiędzy
    różnymi środowiskami programistycznymi.

    Parametry do zapytania QueryParams jako słownik klucz:wartość

    Instrukcje w bloku try jeżeli napotkają jakieś problemy, to zostaną
    wykonane instrukcje z opowiedniego bloku except. Może być dużo bloków
    except a zostanie wywołany tylko ten odpowiedni za każdym razem.
    Blok else wykona się po try
    Finally - zawsze.
'''
"""
    Jeżeli nie podamy parametrów zapytania do stackexchange.com:
    {'error_id': 400, 'error_message': 'site is required', 'error_name': 'bad_parameter'}

    Interesujące zapytanie:
    - Minimalnie 15 punktów.
    - posegregowane malejąco.
    - pytania z ostatniego tygodnia.
    - kategorii Python.


    Wypisane parametry dla pytań na stronie stackoverflow możliwe do skierowania
    do SO API:
    https://api.stackexchange.com/docs/questions#order=desc&sort=activity&filter=default&site=stackoverflow&run=true


    Uzyskanie np. przy pomocy takiego API i programu Python najpopularniejszego
    pytania na stackoverflow:

        params = {
            "site": "stackoverflow",
            "sort": "votes",
            "order": "desc",
        }

    Do lepszego czytania JSON w notepad++:
    Wtyczki --> JSTool --> JSFormat
"""
'''
    Pytania od daty 20 sierpnia 2019:
        params = {
            "site": "stackoverflow",
            "sort": "votes",
            "order": "desc",
            "fromdate": "2019-08-20"
        }

    import pprint dla lepszego formatowania wyświetlanych danych:
    Pretty Print
'''
"""
    JSON z perspektywy Python: listy w słowniku.


    Pytania z kategorii Python z minimum 15 punktów od 20 sierpnia 2019 roku,
    posegregowane malejąco (według głosów) ze strony stackoverflow będącą podstroną
    większego serwisu stackexchange:
        params = {
        "site": "stackoverflow",
        "sort": "votes",
        "order": "desc",
        "fromdate": "2019-08-20",
        "tagged": "python",
        "min": 15
        }
"""
'''
    Otwarcie przetworzonych danych z otrzymanego JSON z API zewnętrznego
    serwisu w przeglądarce:
    items -> link -> to interesuje w tym momencie.


    Wypisanie pojedyńczego pytania z całej listy pytań uzyskanej z danych z
    JSON (listy w słowniku):
        print("question ze słownika questions: ")
        pprint.pprint(question)

    Teraz można odwołać się do konkretnego klucza należącego do pytania
    (question) słownika, np. do konkretnego linku z pytania:

    Otwieranie tych linków przy pomocy modułu webbrowser:
        https://docs.python.org/3/library/webbrowser.html
        import webbrowser
    Strony (zakładki) otworzą się automatycznie w domyślnej przeglądarce.
'''

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": "2019-08-20",
    "tagged": "python",
    "min": 15
}

r = requests.get("https://api.stackexchange.com/2.2/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print(questions)
    print("==============Pretty Print================")
    pprint.pprint(questions)
    for question in questions["items"]:
        print("question ze słownika questions: ")
        pprint.pprint(question)
        print("link ze słownika question: ")
        pprint.pprint(question["link"])
        webbrowser.open_new_tab(question["link"])
