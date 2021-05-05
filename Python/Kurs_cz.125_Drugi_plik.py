from Kurs_cz_125_Zmienne_statyczne_Klasowe import User
'''
    Dostać się do zmiennej klasowej/statycznej można w każdej
    chwili
'''
print("User.name")
print(User.name)
a = User("A_NAME")
b = User("B_NAME")
c = User("C_NAME")
# Zmiana name nie wpływa na instancje nawzajem:

print("a.name")
print(a.name)
print("b.name")
print(b.name)
print("c.name")
print(c.name)

a.name = "newNameA"
b.name = "newNameB"
c.name = "newNameC"

print("a.name")
print(a.name)
print("b.name")
print(b.name)
print("c.name")
print(c.name)

print("\n\n\n\n\n\n\n\n\n\n")

b.name = "totallyNewNameForB"
print("a.name")
print(a.name)
print("b.name")
print(b.name)
print("c.name")
print(c.name)


print("\n\n\n\n\n\n\n\n\n\n")
"""
    Wszelkie zmiany na zmiennej klasowej/statycznej odnośnie konkretnej
    instancji klasy, obiektu, nie wpłyneły na wartość oryginalną name
    w klasie User
"""
print(User.name)

"""
    Robienie ID dla kolejnych elementów.
    dla a = 1, b = 2, c = 3
    Przy każdej inicjalizacji klasy User następuje 
    inkrementacja ID o jeden i przypisanie tak zmienionej
    zmiennej klasowej/statycznej ID do self.id, czyli do ID
    dla konkretnego obiektu, instancji klasy.
    Dzięki temu kolejne instancje tej samej klasy User będą miały
    kolejno numerowane ID.
"""
print("\n\n\n\n\n\n\n\n\n\n")
print("a = 1, b = 2, c = 3")
print(a.id)
print(b.id)
print(c.id)
print("\n\n\n\n\n\n\n\n\n\n")
print("User.id (3)")
print(User.id)
print("\n\n\n\n\n\n\n\n\n\n")







"""
    Wyrażenie listowe:
    8 userów w liście users
    Każdy będzie miał kolejno numerowane ID na zasadzie wyżej opisanej.
    Dzięki takim rozwiązaniom ID już faktycznie jest unikatowe w obrębie
    programu, niezależnie od tego, jaką drogą tworzeni są nowi użytkownicy
    (wyrażenie listowe, przypisanie do zmiennej itd.).
"""
users = [User() for _ in range(8)]

for user in users:
    print(user.id)