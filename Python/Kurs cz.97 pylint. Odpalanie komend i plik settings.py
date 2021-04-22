"""
linter - program do informowania o błędach stylistycznych, 
czyli takich, które nie mają wpływu na
działanie programu, ale mają wpływ na STYL programu

Linter może okazać się przydatny w wieleset linijkowych
programach, automatycznie przypilnuje stylistyki napisanego
kodu.



W Pliku setting.json można dodatkowo ustawić różne
argumenty pracy dla naszego lintera przy pomocy 
instrukcji:
"python.linting.pylintArgs": []
i np. dla flake8:
--ignore-W292,F601
Ignorowanie pilnowania, czy na końcu Pythonowego pliku
jest zawsze nowa linia.
Po przecinku wpisywanie kolejnych rzeczy do zignorowania,
numery W292, F601 bierze się z zakładki Problems w VSC z 
komunikatów od lintera.




Można uruchomić wiele linterów na raz.
Każdy linter będzie miał troszeczkę inne zasady pilnowania
kodu ustalone przez kogoś.
Może któryś z linterów będzie miał lepsze opisywanie
problemów zgłaszanych w komunikatach w zakładce Problems, może 
być i tak.




Odinstalowywanie pakietów, też linterów:
pip uninstall nazwa_litera


Wykrywanie błędów mających wpływ na działanie programu w kodzie:
interpreter


CTRL + SHIFT + P --> uruchomienie komend, co ma się stać w VSC
CTRL + P i napisać '?' aby dowiedzieć się, co można tam robić
"""

pokoje = {49: 'Arkadiusz Włodarczyk', 69: 'Wioletta Włodarczyk'}

a = {'imie': 'Arkadiusz', 'nazwisko': 'Włodarczyk', 'imie': "Wiola"} 
 

sam = 4
sampleNumber = 4


def get_number():
    return 5

print(get_number())