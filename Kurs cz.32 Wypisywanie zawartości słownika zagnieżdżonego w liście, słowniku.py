people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }
"""
[('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
 ('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}),
 ('yDlgcn99xPc19mYXcRmy', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('cpQh6GiAbBdGv35NDoTk', {'name': 'Nabeel', 'age': 17, 'sex': 'Male'}),
 ('12BifzWxCQySKgLhgahC', {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'}),
 ('QLnmg0pzlLj9x7c7DlLv', {'name': 'Ruby', 'age': 55, 'sex': 'Female'}),
 ('To47urX0DUznWmOxGZ6H', {'name': 'Lori', 'age': 27, 'sex': 'Male'}),
 ('KQ4bir3y4tlkbG69I7zq', {'name': 'Marie', 'age': 42, 'sex': 'Female'}),
 ('94cp4hsyZP2BnCh4D34z', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('Vr4wRdkljeEs46Czxo54', {'name': 'Chiara', 'age': 17, 'sex': 'Male'})]

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]


for name, age, sex in ppllist2:
    print(name)

"""
# Lista, elementy to słowniki
people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
          ]

# Słownik. Wartościami są krotki.
ratings1 = {
            "Arkadiusz": (2,1,2,3,2,3),
            "Agness": (4,2,1,3,4)           
           }    
ratings2 = [
        {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
    ]

ratings3 = {
        "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        "Agness:": {'ratings': (4,2,1,3,4), 'behaviour': 2}
    }

print("\n\n\n\n\n\n")
print("ratings1: ")
for key in ratings1:
    print(key, "oceny", ratings1[key])


print("\n\n\n\n\n\n")
print("people3: ")
for value in people3:
    print(value)


print("\n\n\n\n\n\n")
print("people2: ")
for value in people2:
    print(value)


print("\n\n\n\n\n\n")
for dictionary in people2: # Każdy element listy nazwany jako dictionary
    for key in dictionary: # Każdy ten słownik ma KLUCZ
        print(key, ":", dictionary[key]) # Wyświetlenie wartości przypisanej do KLUCZA



# Słownik, do swoich KLUCZY ma przypisane wartości będące innymi słownikami z danymi.
print("\n\n\n\n\n\n")
print(people["IcFDG2bO9AYDF651DoyH"])
for key in people: # KLUCZ ze słownika people
    print("ID:", key)
    for secondaryKey in people[key]: # people[key] <-- sięgamy do słownika przypisanego do klucza głównego.
        print(secondaryKey, ":" , people[key][secondaryKey]) # Wypisanie klucz : wartość
        # people[KLUCZ_GŁÓWNY][PODKLUCZ Z PODSŁOWNIKA] = przypisana do tego wartość





print("\n\n\n\n\n\n")
# Metoda items() jest dostępna tylko w przypadku słowników.
# O wiele prostsze wypisywanie danych z takiej konstrukcji.
# KLUCZ_GŁÓWNY, PODSŁOWNIK
# Wypisanie głównego klucza,
# Dla każdego klucza w podsłowniku wypisanie klucz : wartość
'''
    Używanie podejścia z użyciem metody items() jest dużo szybsze od
    tradycyjnego podejścia.
    Będzie to zauważalne w przypadku przetwarzania bardzo dużej ilości
    danych.
'''
for id, dictionary in people.items():
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])
