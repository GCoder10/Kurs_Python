"""
    Użytkownik o ID ile ukończył zadań
    {
        1: 11
        2: 6
    }


    completedTaskFrequencyByUser.items() <-- Uzyskanie listy krotek,
    dzięki czemu można przechodzić prosto pętlą for i zliczać/porównywać itp.
    para wartość ()

    completedTaskFrequencyByUser.values() <-- Wybranie w liste samych wartości
    przypisanych do kluczy, następnie przekazanie tego do funkcji max(), czyli:
    max(completedTaskFrequencyByUser.values()) <-- w ten sposób wybranie
    użytkownika, który wykonał najwięcej zadań.
"""
import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_task_frequency(tasks):
    print("Wszystko jest okej")
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        print(entry)
        if (entry["completed"] == True):
            try: # W kolejnych razach to będzie wykonywane
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError: # Pierwsze dodanie do pustego słownika
                completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser


def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]  

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask): # Jeżeli idziemy
        # przez krotke, która ma akurat największą ilość wykonanych zadań, to ten
        # user wykonał najwięcej zadań.
            print("Najwięcej zadań wykonał userId: ")
            print(userId)
            userIdWithMaxCompletedAmountOfTasks.append(userId) # Dodawanie
            # użytkowników (ich ID), którzy wykonali najwięcej zadań do listy.
            print("Lista userId najwięcej ukończonych zadań: ")
            print(userIdWithMaxCompletedAmountOfTasks)
    return userIdWithMaxCompletedAmountOfTasks
try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    print("get_users_with_top_completed_tasks(completedTaskFrequencyByUser): ")
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print(usersWithTopCompletedTasks)
    print("Nagroda dla userId: ", usersWithTopCompletedTasks)
print("completedTaskFrequencyByUser: ")
print(completedTaskFrequencyByUser)
print("=================================================")
print("Uniwersalna funkcja do liczenia, który klucz ma największą przypisaną wartość w słowniku: ")
print(get_keys_with_top_values(completedTaskFrequencyByUser))
print("=============Users===========================")            

# =============================  Sposób pobrania userów 1 ==========================
response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()
print(users)
for user in users: # Spr. czy userId w pobranych danych z użytkownikami z serwera
    # znajdują się userId z listy usersWithTopCompletedTasks i wypisanie ich
    # danych.
    if(user["id"] in usersWithTopCompletedTasks):
        print("ID: ", user["id"])
        print("imie: ", user["name"])

# =============================  Sposób pobrania userów 2 ==========================
