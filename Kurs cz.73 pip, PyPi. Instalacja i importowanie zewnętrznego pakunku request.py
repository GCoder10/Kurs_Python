"""
    pip - pip installs packages - instalator pakunków

    PyPi - Python Package index - indeks (spis) pakunków do Python
    Strona pypi.org
    Wyszukanie requests
    Instalacja: pip install requests
    cmd -> pip install requests


    Po uruchomieniu, po wpisaniu w IDLE:
    response200OK
    <Response [200]> status OK, pobrano zawartość ze strony


    Jeżeli wystąpi błąd, np. strona nie istnieje:
    <Response [404]> status nie znaleziono


    Pobieranie zawartości strony, DOCTYPE, dalej coś z tym robić
    w programie + np. jeżeli response.status_code == 200 to coś robić itp.

    Przykład pobranej strony wp.pl za pomocą requests.get w pliku
    wpSiteExampleRequestsGet.txt
"""
import requests

response200OK = requests.get("https://www.wp.pl")

print(response200OK)


response404 = requests.get("https://www.wp.pl/ssxsxs")

print(response404)


# requests zwraca obiekt, czyli coś, co ma właściwości.
# Można to wykorzystać, jeżeli status_code == 200 to coś dalej itp.
print("print(response200OK.status_code): ")
print(response200OK.status_code)


print("print(response200OK.text): ")
print(response200OK.text)
