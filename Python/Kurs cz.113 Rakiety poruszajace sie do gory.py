"""
    __init__ - initialization - inicjalizacja - czyli ustawienie
    startowych wartości dla atrybutów.


    W innych językach __init__ to konstruktor.
    Konstruktor nowych obiektów.
    Wywołuje się zawsze podczas tworzenia obiektu na podstawie
    klasy, w której się znajduje.


    Dalej operowanie na self. czyli odwołanie się do argumentu
    należącego do konkretnego obiektu (instancji tej klasy).


    Klasa Rocket, 5 instancji tej klasy, początkowe wartości
    wysokości, losowe poruszanie rakietami o losową wartość 
    do góry.
""" 

class User:
    def __init__(self, age, name):
        print("User.__init__")
        self.age = age
        self.name = name
        ageInFuture = age + 1
        print("Zmienna tylko lokalnie w konstruktorze:", ageInFuture)
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

user1 = User(30, "imie_user1")
user2 = User(29, "imie_user2")


userList = [User(99, 'imie_99'), User(100, 'imie_100')]

print(userList)

userList[0].print_name()
userList[0].print_age("[userList[0]] Dodatkowy tekst", "[userList[0]] kolejny argument")

userList[1].print_name()
userList[1].print_age("[userList[1]] Dodatkowy tekst", "[userList[1]] kolejny argument")

print("\n\n\n\n\n\n\n\n")

user1.print_name()
user1.print_age("[user1] Dodatkowy tekst", "[user1] kolejny argument")

user2.print_name()
user2.print_age("[user2] Dodatkowy tekst", "[user2] kolejny argument")