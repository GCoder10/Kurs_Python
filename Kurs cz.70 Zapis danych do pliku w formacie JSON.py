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
    json.dumps(data) - zapisuje dane do postaci stringowej json
    dumps przetwarza np. polskie znaki przy pomocy tablicy ASCII,
    próbuje tak zrobić, dlatego się nie udaje.
    ensure_ascii = False
    Nie używanie tablicy ascii do przetwarzania znaków.


    
    
    json.dump(data, nameOfFile, ensure_ascii = False) - zapisuje dane
    do pliku w postaci json.

    dump z ang. zsypać/zwalić/zrzucać

    Zrzucamy dane (data) do postaci json
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

print(json.dumps(film))
print("\n\n\n\n\n")
print(json.dumps(film, ensure_ascii = False))
print("\n\n\n\n\n")
print("encodedFilm: ")
encodedFilm = json.dumps(film, ensure_ascii = False)
print(encodedFilm)


with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii = False)

"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

