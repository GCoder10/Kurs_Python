# Słownik w słowniku. Wartością dla KLUCZA jest cały słownik
# Dodawanie dużej ilości elementów będzie szybsze do słownika.
# Z faktu, iż nie liczy się kolejność.
'''
    Przeszukiwanie słownika jest także wiele razy szybsze przy dużej
    ilości przechowywanych danych niż w listach. W liście trzeba użyć
    pętli, aby znaleźć dane przypisane do ID, natomiast w słowniku
    można od razu sięgnąć po dane przypisane do ID bez przeszukiwania
    w tym celu całego słownika.
'''
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
        "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
        "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
        "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
        "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
        "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}           
         }

# Słownik w liście. Dodawanie dużej ilości elementów będzie wolniejsze z
# uwagi na fakt, iż liczy się kolejność w liście.
people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
          ]


# Słownik z ocenami. Krotka jako wartość dla KLUCZA
oceny = {
            "Arkadiusz": (2,1,2,3,2,3),
            "Wiola": (4,2,1,3,4)
        }



"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]
for name, age, sex in ppllist2:
    print(name)

"""

print(oceny["Arkadiusz"])
print(people["KQ4bir3y4tlkbG69I7zq"])
