"""

JSON
Przekazywanie danych między różnymi środowiskami programistycznymi.
KLUCZE: wartości
słownik
Wspólny format danych - json
posiada pewne reguły zapisu danych.
Metody zamieniające nasz typ danych na json.
W innym środowisku programistycznym odczytanie tych danych przy pomocy
odpowiednich metod.

Słownik i lista - json

"""
'''
    json.loads(jsonstring) - przetwarza jsonstring na dane typu Python

    json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody
    dane typu Python
    filePointer - wskaźnik na plik - uchwyt - file


    Ktoś nam przysłał dane w json
    
'''
import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedMovie = json.loads(encodedRetrievedMovie)
print("decodedMovie: ")
print(decodedMovie)


with open("sample.json", encoding = "UTF-8") as file:
    jsonDataFromFile = json.load(file)
    print("JSON data from file: ")
    print(jsonDataFromFile)


