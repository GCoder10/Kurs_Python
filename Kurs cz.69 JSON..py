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

"""

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

