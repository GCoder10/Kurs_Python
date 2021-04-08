'''
    indent = 4
    sort_keys = True
    indent - ang. Wcięcie

    sort_keys - sortowanie kluczy słownika, sortowanie alfabetyczne, "title",
    "credits" itd <- Klucze tutaj.
    
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

encodedFilm = json.dumps(film, ensure_ascii = False, indent = 4, sort_keys = True)
print("encodedFilm: ")
print(encodedFilm)


with open("sample2.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii = False, indent = 4, sort_keys = True)



with open("sample.json", encoding="UTF-8") as file:
    jsonDataFromFile = json.load(file)
    print("jsonDataFromFile before sort: ")
    print(jsonDataFromFile)
    print("\n\n\n\n")
    print("jsonDataFromFile sorted: ")
    print(json.dumps(jsonDataFromFile, ensure_ascii = False, indent = 4, sort_keys = True))


import pprint # Pretty Print

print("\n\n\n\n")
print("pprint: ")
pprint.pprint(jsonDataFromFile)
