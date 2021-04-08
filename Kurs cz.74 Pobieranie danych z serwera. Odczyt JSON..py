"""
    JSONplaceholder - miejsce zastępcze na przyszły json.

    Który użytkownik robi najwięcej zadań.
    ID zadania, użytkownik, treść zadania, bool czy wykonano
    Skorzystanie z gotowych danych json.
    JSONplaceholder - połączenie
    JSONplaceholder.typicode.com <-- przykładowe dane json do ćwiczeń / testowania
    programu / projektu.

    Resources - zasoby - jakieś częste aspekty występujące
    jsonplaceholder.typicode.com/todos <-- lista zadań, co kto wykonał
"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
response2 = requests.get("https://wp.pl")
print("Pobrane dane ze strony jsonplaceholder.typicode.com/todos: ")
print(response.text)


tasks = json.loads(response.text)
print("tasks[0]")
print(tasks[0])
print("tasks[10]")
print(tasks[10])
print("tasks[15]")
print(tasks[15])
print("tasks[:10]") # Pierwsze 10 elementów
print(tasks[:10])
print("tasks[10:20]") # Od 11 do 20 elementu
print(tasks[10:20])


tasks2 = response.json() # To samo co json.loads(response.text), ale krócej
# Dodatkowo sprawdza, czy pobierane dane są na pewno json.

try:
    tasks3 = response2.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko jest okej") # Wykona się, gdy instrukcje w bloku
    # try wykonają się bez błędów.
    # Może być wiele except, ale zostanie wybrany tylko ten z błędem,
    # który akurat wystąpił podczas wykonywania się instrukcji w bloku
    # try.
