"""
    Domyślne wartości dla kluczy, np. gdy odwołamy się do klucza, który
    nie istnieje, zostanie zwrócona taka domyślna wartość.
    A dokładniej jakiego typu

        a:  defaultdict(<class 'int'>, {'55': 0})
        b:  defaultdict(<class 'float'>, {'55': 0.0})
        c:  defaultdict(<class 'str'>, {'55': ''})

    Klucz posiada domyślną wartość w przypadku, gdy nie istnieje, typ domyślnej
    wartości.
"""
"""
    
"""
import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")

from collections import defaultdict

a = defaultdict(int)
b = defaultdict(float)
c = defaultdict(str)

print("a['55']: ", a["55"])
print("b['55']: ", b["55"])
print("c['55']: ", c["55"])
print("a: ", a)
print("b: ", b)
print("c: ", c)

def count_task_frequency(tasks):
    print("Wszystko jest okej")
    completedTaskFrequencyByUser = defaultdict(int)
    for entry in tasks:
        print(entry)
        if (entry["completed"] == True):
            completedTaskFrequencyByUser[entry["userId"]] += 1
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
print("\n\n\n\n\n\n\n\n")


response5 = requests.get("https://jsonplaceholder.typicode.com/users/5")
user5 = response5.json()
print("user5: ")
print(user5)
print("ID: ", user5["id"])
print("imie: ", user5["name"])
print("\n\n\n\n\n\n\n\n")
print("========================================================")

"""
    W celu mniejszego obciążenia serwera przy bardzo dużej ilości danych należy
    pobrać najpierw dane wszystkich użytkowników do komputera a potem przetwarzać
    te dane (filtrowanie, sortowanie, szukanie itp.) dopiero w programie.
    O wiele optymalniejsze rozwiązanie, takie oddzielne pobieranie to najwyżej gdy jest
    pewność, że jest naprawdę mało danych.
"""
for userId in usersWithTopCompletedTasks: # Wykonanie tylu połączeń do serwera w celu
    # pobrania danych o userach, ile userId jest w liście usersWithTopCompletedTasks
    # Dla każdego usera pobiera się dane oddzielnie.
    response = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    user = response.json()
    print("ID: ", user["id"])
    print("imie: ", user["name"])
print("========================================================")



for userId in usersWithTopCompletedTasks: # QueryParams
    response = requests.get("https://jsonplaceholder.typicode.com/users/", params = "id=5")
    print("user5 QP: ")
    user = response.json()
    print(user)


print("========================================================")



for userId in usersWithTopCompletedTasks: # QueryParams
    response = requests.get("https://jsonplaceholder.typicode.com/users/", params = "id=" + str(userId))
    print("users QP: ")
    user = response.json()
    print("ID: ", user[0]["id"])
    print("imie: ", user[0]["name"])



# =============================  Sposób pobrania userów 3 ==========================
print("\n\n\n\n\n\n\n\n")
print("=========================Sposób 3===============================")
# Podawanie wielu id jednocześnie do jednego zapytania. QueryParams
'''
    Funkcja change_list_into_conj_of_param zamieniająca wartości listy, np. z id na
    QP, na parametry możliwe do przesłania jako argument do zapytania do serwera, w celu
    pobrania danych tych wybranych użytkowników (wtedy wszystkich na raz)
    key = wartość string, z którego będzie składało się zapytanie, zamiast id --> key
'''
response = requests.get("https://jsonplaceholder.typicode.com/users/", params = "id=5&id=10")
users = response.json()

def change_list_into_conj_of_param(my_list):

    return "id=5&id=10"

for user in users:
    print("ID: ", user["id"])
    print("imie: ", user["name"])


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks)
response = requests.get("https://jsonplaceholder.typicode.com/users/", params = conj_param)
users = response.json()
print("conj_param: ")
print(users)

print("\n\n\n\n\n\n\n\n")


def change_list_into_conj_of_param(my_list, key = "id"):
    conj_param = key + "="

    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else: 
            conj_param += str(item) + "&" + key + "="
    return conj_param


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")
response = requests.get("https://jsonplaceholder.typicode.com/users/", params = conj_param)
users = response.json()
print("usersWithTopCompletedTasks, 'id': ")
for user in users:
    print("ID: ", user["id"])
    print("imie: ", user["name"])
print("\n\n\n\n\n\n\n\n")


conj_param = change_list_into_conj_of_param([2,7,4], "id")
response = requests.get("https://jsonplaceholder.typicode.com/users/", params = conj_param)
users = response.json()
print("[2,7,4], 'id': ")
for user in users:
    print("ID: ", user["id"])
    print("imie: ", user["name"])
