"""
    1. Logowanie --> login, hasło
        Spr. loginu i hasła
    2. Pobranie z bazy danych userId i username
    3. Pokazanie dla konkretnego zalogowanego usera jego ulubione kotki,
    umożliwienie dodania kolejnego, losowego też, usuwanie.

    Pobieranie kotków powiązanych z kontem usera:
        https://docs.thecatapi.com/api-reference/favourites/favourites-list
            Generalnie zostaną zwrócone dane kotków dla api_key ale jest jeszcze
            'sub_id', pod_id_konta, sub konta, pod konta
            Czyli sub_id reprezentuje userów pochodzących z naszego programu, więc
            to są takie sub konta z perspektywy zewnętrznego API.


    Funkcja get_favourite_cats(userId):
        Wysłanie jako params sub_id oraz jako nagłówek (headers) API_KEY
        jednocześnie.
        Pobranie ulubionych kotków przy użyciu naszego głównego API_KEY
        dla zalogowanego użytkownika naszego programu.
"""
'''
    Funkcja get_json_content_from_response(response):
        Wyciąganie zawartości z JSON z odpowiedzi z backendu.
'''
"""
    Funkcja - gdy jest return, zwraca jakieś dane jakiegoś typu.
    Procedura - void z C++/C++11 - nie zwraca nic.
"""
'''
    Funkcja get_random_cat
    https://docs.thecatapi.com/api-reference/images/images-search
    Obrazek losowego kotka.
    Dostanie się do zwróconej zawartości i zwrócenie tej zawartości z
    JSON z serwera jako:
        return get_json_content_from_response(r)

    Zwrócone zostaje to jako lista słowników zawierająca jednego kotka,
    każdy następny byłby zapisany jako kolejny słownik w tej liście.
    Klucz "url": jego wartością jest adres do zdjęcia wylosowanego tak kotka.
'''
"""
    POST wysyłanie danych do serwera, jako JSON najczęściej, parametry, nagłówek
    to już w ogóle głównie jest JSON.
    W tym przypadku zdjęcie zostanie przypisane do konta głównego korzystającego
    z zewnętrznego API (API_KEY) oraz zostanie dodane, do kogo należy to zdjęcie
    (sub_id):
        https://docs.thecatapi.com/api-reference/favourites/favourites-post


    def add_favourite_cat(catId, userId):
        Dodawanie polubionego kotka dla użytkownika, który go polubił.
        W zapytaniu typu POST dajemy BASE URL serwera, dane do przesłania
        jako słownik, przypisane wartości a następnie przypisanie tego do
        argumentu nazwanego json, który automatycznie zamieni takie dane na typ
        JSON. Dodatkowo można dodać nagłówek oczywiście też (z poufnymi danymi
        logowania [API_KEY/Token]).
        Tak przygotowane dane można przysłać do backendu wykonanego np. w C# (
        do backendów wykonanych w innych środowiskach programistycznych także).
        Zwrot tutaj ze strony backendu następuje jako JSON, słownik, zawierający
        wiadomość o błędzie lub sukcesie i ID tego komunikatu (tutaj jest to ID
        w favourites jakie to ma).
        Jest to ID rekordu w bazie backend z ulubionym nowym kotkiem.


    Każdy użytkownik jak już ma dodane kotki, to jego polubione kotki zostają zwrócone
    jako lista słowników, gdzie każdy ze słownika w tej liście reprezentuje dane
    każdego polubionego kotka oddzielnie.
"""

import requests
import json
import webbrowser
import Kurs_cz87_Credentials
from pprint import pprint

def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params,
                     headers = Kurs_cz87_Credentials.headers)
    return get_json_content_from_response(r)

def get_json_content_from_response(response):  
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format", response.text)
    else:
        return content


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers = Kurs_cz87_Credentials.headers)
    return get_json_content_from_response(r)


def add_favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json = catData,
                     headers = Kurs_cz87_Credentials.headers)
    return get_json_content_from_response(r)    

print("Podaj login i hasło")

userId = "agh2m"
name = "Imie"

print("Witaj " + name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione kotki to:", favouriteCats)

randomCat = get_random_cat()
print("Wylosowano kotka:", randomCat)


randomCat = get_random_cat()
print("Pierwszy kotek (słownik) z listy --> randomCat[0]['url']:", randomCat[0]["url"])
addToFavourites = input("Czy chcesz dodać do ulubionych tego kotka? T/N")
if (addToFavourites.upper() == "T"):
    print("add_favourite_cat(randomCat[0]['id'], userId): ")
    print(add_favourite_cat(randomCat[0]["id"], userId))
    add_favourite_cat(randomCat[0]["id"], userId)
else:
    print("Nie dodano kotka do ulubionych")
