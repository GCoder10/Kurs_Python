"""
    OOP - Object Oriented Programming

    Programowanie zorientowane wokół obiektów.

    Obiekty - przechowywanie zmiennych oraz funkcji tematycznie
    ze sobą powiązanych do ponownego ich użycia.

    Klasy - szablony do tworzenia egzemplarzy obiektów,
    czyli obiekt to instancja klasy,
    to samo co było w C++/C++11.
    Obiekt reprezentuje daną klasę i daje nam dostęp do 
    funkcji, metod, procedur itp. tam istniejących, 
    wykonywanie różnych zadań przy pomocy takich funkcji
    pochodzących z innej klasy.
    Funkcje takie mogą też zwracać dane określonego typu
    poprzez return.


    Atrybut = cecha
""" 

class User:
    age = 0
    # pass # pomija wykonanie czegokolwiek

seba = User()
mirek = User()
'''
    <__main__.User object at 0x000001C69C08DF70>

    main - odwołanie do faktu, iż obiekt klasy User znajduje się
    w głównym pliku programu.
    at - w adresie (przechowywany) Hexadecimal, to samo co
    adresy w C++/C++11


    seba i mirek to inne obiekty, są przechowywane w innych miejscach
    w pamięci (różne adresy):

    <__main__.User object at 0x0000011CC1B5DF70>
    <__main__.User object at 0x0000011CC1B5DFD0>


    Dwa różne obiekty, dwie różne instancje klasy, dwa różne
    adresy przechowywania tych obiektów, czyli mogą być te same
    nazwy atrybutów dla wielu obiektów.
    Zmienna o tej samej nazwie co nazwa atrybutu, nie ma wpływu,
    jest przechowywana pod jeszcze innym adresem (3-cim).


    Dlaczego nie dict()? tylko klasa:
    Bo w klasie określamy nie tylko atrybuty ale także metody.
'''
seba.age = 16
mirek.age = 24

age = 40
print(seba) 
print(mirek)
seba.age = 20
print(seba.age) 
print(mirek.age)
print(age)

x = 5.4
print(x)
print(type(x))
# Zmienna x jest obiektem.
# <class 'float'> klasy float, instancja klasy float



print(type(mirek))
# <class '__main__.User'> Obiekt klasy User znajdującej się
# w głównym module programu, miejscu main
# typ klasowy.



print(x.is_integer())
x = 5.0
print(x.is_integer())

# Natomiast obiekt klasy integer nie ma metody is_integer()
# x = 5
print(x.is_integer())
# 'int' object has no attribute 'is_integer'

# Gdy usunie się atrybut z np. seba, age, to wyskoczy ten sam
# błąd (tej samej logiki), że nie ma atrybutu w obiekcie
# klasy User
# Jeżeli chcemy, żeby wszędzie były metody/atrybuty (koniecznie
# w każdej instancji klasy), to trzeba zadeklarować to w samej
# klasie.