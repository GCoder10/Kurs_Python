"""
    VSC -> Extension -> Bracket Pair Colorizer 2
    by CoenraadS

    Fajny dodatek dla czytelności
"""
import json

film = {
    "title": "Example Title 1",
    "release_year": 1980,
    "won_oscar": True,
    "actors": {"Name Surname 1","Name Surname 2"},
    "budget": None,
    "credits": {
        "director": "Name Surname Director",
        "writer": "Name Surname Writer",
        "animator": "Name Surname Animator"
    }
}

encodedFilm = json.dumps(film, ensure_ascii = False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dumps(film, file, ensure_ascii = False)