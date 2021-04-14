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
'''
    Zapytanie DELETE do usunięcia polubionego kotka przez użytkownika naszego programu:
        https://docs.thecatapi.com/api-reference/favourites/favourites-delete
    Wyrażenie słownikowe do wybrania id kotka z jednego ze słowników z listy ulubionych kotków
    uzyskiwanej przy użyciu funkcji:
        def get_favourite_cats(userId):


    favouriteCat["id"]: favouriteCat["image"]["url"]
    for favouriteCat in favouriteCats
    Takie wyrażenie słownikowe pozwoli utworzyć nowy słownik automatycznie dla każdego kotka w
    polubionych kotkach, kluczem będzie ID kotka a wartością adres url do zdjęcia.
    Zdjęcie "image" jest kluczem, którego wartością jest kolejny słownik, więc po adres URL
    trzeba zasięgnąć głębiej (klucz ["url"]: wartość to adres do zdjęcia).


    Funkcja usuwająca:
        def remove_favourite_cat(userId, favouriteCatId):
    sub_id użytkownika, ID kotka podana przez niego do usunięcia.

    Backend obsłuży zapytanie jak dodamy tylko jako QueryParams do końca zapytania ID:
        'https://api.thecatapi.com/v1/favourites/' + favouriteCatId
    np. w C#, po routingu backendu jesteśmy w bloku instrukcji odpowiedzialnym za endpoint favourites
    i gdy typ zapytania to DELETE, to odpowiednio przygotowane instrukcje pobiorą ID z otrzymanego adresu wraz z
    zapytaniem i następnie zostanie usunięte zdjęcie o podanym ID z bazy (Entity Framework).
'''
"""
    Optymalizacja i refaktoryzacja:
        Jak najmniej zapytań do serwera, przy większej obróbce danych najpierw pobieranie wszystkiego
        do programu a potem dopiero filtrowanie, sortowanie, analizowanie danych itp. a nie ciągle
        wysyłanie w tym celu zapytań do serwera. Program zrobi to szybciej, nie trzeba posiadać szybkiego
        łącza przy większej ilości danych i nie obciążamy zbędnie serwera.

        Wykorzystywanie danych, które już są w programie, bez zbędnego pytania serwera o wszystko, np.:
        Po dodaniu ulubionego kotka przez użytkownika o sub_id, zamiast pytać serwer o listę słowników
        ulubionych kotków, zaktualizowanie już obecnego słownika favouriteCatsById (wyrażenie słownikowe)
        o nowe dane z newlyAddedCatInfo:
            print("Zamiast add_favourite_cat(randomCat[0]['id'], userId), to: ")
            resultFromAddingFavouriteCat = add_favourite_cat(randomCat[0]["id"], userId))
            newlyAddedCatInfo = {resultFromAddingFavouriteCat["id"] : randomCat[0]["url"]}
        favouriteCatsById.update(newlyAddedCatInfo)
        Update wyrażenia słownikowego danymi z nowego słownika.

        randomCat sugeruje, że dane dotyczą jednego kota, więc po co lista zawierająca słownik dla jednego
        kota, skoro zawsze będzie to tylko jeden kot, nie potrzeba wtedy listy ze słownikiem w środku.
        Trzeba zrobić tak, aby dało się odwołać do ID kotka nie w takich sposób: randomCat[0]['id'],
        tylko za pomocą: randomCat['id'], czyli od razu sam słownik.
            def get_random_cat():
                r = requests.get('https://api.thecatapi.com/v1/images/search',
                                 headers = Kurs_cz87_Credentials.headers)
                return get_json_content_from_response(r)[0]
        Od razu w funkcji get_random_cat zwracamy ten pierwszy element, czyli:
            return get_json_content_from_response(r)[0]
        i ostatecznie randomCat od razu posiada tylko jeden słownik.

        Dzielenie programu na mniejsze części, np. jak w multiAPI w C++/C++11, dbanie w ten sposób
        o czytelność kodu w najważniejszych modułach programu.
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
    return get_json_content_from_response(r)[0]


def add_favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json = catData,
                     headers = Kurs_cz87_Credentials.headers)
    return get_json_content_from_response(r)


def remove_favourite_cat(userId, favouriteCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' + favouriteCatId,
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
print("Pierwszy kotek (słownik) z listy --> randomCat['url']:", randomCat["url"])
addToFavourites = input("Czy chcesz dodać do ulubionych tego kotka? T/N")
if (addToFavourites.upper() == "T"):
    print("Zamiast add_favourite_cat(randomCat[0]['id'], userId), to: ")
    resultFromAddingFavouriteCat = add_favourite_cat(randomCat["id"], userId)
    newlyAddedCatInfo = {resultFromAddingFavouriteCat["id"] : randomCat["url"]}
else:
    print("Nie dodano kotka do ulubionych")


favouriteCatsById = {
    favouriteCat["id"]: favouriteCat["image"]["url"]
    for favouriteCat in favouriteCats
}
favouriteCatsById.update(newlyAddedCatInfo)


print("favouriteCatsById: ")
print(favouriteCatsById)

favouriteCatId = input("Kotka o którym ID chcesz usunąć?: ")

print("remove_favourite_cat(userId, favouriteCatId): ")
print(remove_favourite_cat(userId, favouriteCatId))
