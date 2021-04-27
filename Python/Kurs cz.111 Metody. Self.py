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

    self - z ang. 'ja', 'sam osobiście', 'siebie', w innych
    językach 'this'.


    Jako pierwszy parametr metody w klasie musi być argument
    self.
    W innych językach: this
    Self jest tutaj obowiązkowy i występuje jako parametr
    pierwszy w metodzie, każdej.
    Odwołując się wtedy do cech opisujących obiekt, trzeba
    napisać self przed nazwą argumentu:
    self.age

    Self został tak zaprojektowany, że nie wchodzi w 
    interakcję z przesyłanymi argumentami do metody w 
    klasie, zostaje automatycznie dodany, ale w samej klasie
    trzeba go samemu zadeklarować. 



    Nazwy klas należy rozpoczynać od wielkiej litery.
""" 

class User:
    age = 0
    name = ""
    # pass # pomija wykonanie czegokolwiek
    def print_age(self, message, message2):
        print("[User.print_age] wiek:", self.age)
        print("[User.print_age] wiadomość:", message)
        print("[User.print_age] wiadomość2:", message2)
    def another_method(self):
        pass
    def another_method2(self, args):
        pass 
    def print_name(self):
        print("[User.print_name] imie:", self.name)

seba = User()
mirek = User()
imie = User()
user1 = User()
user2 = User()


userList = [User(), User()]
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

def print_age(name, age):
    print(name, 'wiek:', age)

name = 'Imie'
print_age(name,age)


# Wywala błąd o 0 oczekiwanych argumentach przez metodę
# print_age a otrzymał niby jedną, jest to domyślny, 
# 'niewidzialny' argument - self:
# mirek.print_age(self)
# Bez mirek.age = 24 będzie 0, czyli wartość domyślna 
# ustawiona w klasie User.
mirek.print_age(" ", " ")

print("\n\n\n\n\n\n\n")

mirek.print_age("Dodatkowy tekst", "kolejny argument")


print("\n\n\n\n\n\n\n")
'''
    Oczywiście jak było wspominane, obiekty mają oddzielne adresy,
    nie wpływają na siebie, tak samo różne zmienne, będące instancją
    klasy typ_zmiennej.
'''

imie.age = 33
imie.print_age("[imie] Dodatkowy tekst", "[imie] kolejny argument")

mirek.age = 44
mirek.print_age("[mirek] Dodatkowy tekst", "[mirek] kolejny argument")


print("\n\n\n\n\n\n\n")



user1.age = 29
user1.name = "Imie1Usera1"
user1.print_age("[user1] Dodatkowy tekst", "[user1] kolejny argument")
user1.print_name()

user2.age = 30
user2.name = "Imie2Usera2"
user2.print_age("[user2] Dodatkowy tekst", "[user2] kolejny argument")
user2.print_name()






print("\n\n\n\n\n\n\n")
'''
    Dwa obiekty klasy User
    Dalej odwoływanie się do userów z tej listy
'''
print(userList)
userList[0].age = 99
userList[1].age = 100
userList[0].name = 'imie_99'
userList[1].name = 'imie_100'

userList[0].print_name()
userList[0].print_age("[userList[0]] Dodatkowy tekst", "[userList[0]] kolejny argument")

userList[1].print_name()
userList[1].print_age("[userList[1]] Dodatkowy tekst", "[userList[1]] kolejny argument")
