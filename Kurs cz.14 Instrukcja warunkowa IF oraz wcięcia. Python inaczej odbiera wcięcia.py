"""
    Instrukcja warunkowa
        Jeśli (PRAWDA)
            To...
        Jeśli co innego (PRAWDA)
            To...
        A całkowicie w innym przypadku
            To...

    elif - else if
"""

# po wyrażeniu takim : musi być
# Wcięcie pod instrukcją warunkową musi być
# Wcięcia w Python'ie określają, jakie instrukcje dotyczą powyższej instrukcji warunkowej.
if (5 > 3):
    print("5>3 PRAWDA")

if (5 < 3):
    print("5<3 FAŁSZ")

if (100 > 99):
    print("100 > 99 PRAWDA 1")
    print("100 > 99 PRAWDA 2")
    print("100 > 99 PRAWDA 3")

if (100 == 99):
    print("100 == 99 FAŁSZ 1")
    print("100 == 99 FAŁSZ 2")
    print("100 == 99 FAŁSZ 3")
print("100 == 99 FAŁSZ 4 - Wykona się")

# W innych językach wcięcia są głównie po to, żeby ładniej wyglądał kod, natomiast w Python
# mają znaczenie.
# Ilość spacji we wcięciu też ma znaczenie w odwoływaniu się do konkretnej instrukcji
# warunkowej.
'''
Błąd:
if (100 > 99):
  print("100 > 99 PRAWDA 1")
    print("100 > 99 PRAWDA 2")
'''
# W założeniu powinno się dawać 4 spacje, mogą być dwie.
# TAB przez ten edytor (IDLE) jest zamieniany na 4 spacje.

a = int(input("Podaj wartość liczby a "))
b = int(input("Podaj wartość liczby b "))

if (a > b):
    print("a jest większe od b")
elif (b > a):
    print("b jest większe od a")
else:
    print("a jest równe b")


# Wybór z menu:
print("1 - mnożenie")
print("2 - dzielenie")
print("3 - dodawanie")
print("4 - odejmowanie")
wybor = input()
c = int(input("Podaj wartość liczby c "))
d = int(input("Podaj wartość liczby d "))

if (wybor == '1'):
    print("Mnożenie liczb:", c, "*", d, "=", c*d)
elif (wybor == '2'):
    if (d == 0):
        print("Nie dziel przez zero")
    else:
        print("Dzielenie liczb:", c, "/", d, "=", c/d)
elif (wybor == '3'):
    print("Dodawanie liczb:", c, "+", d, "=", c+d)
elif (wybor == '4'):
    print("Odejmowanie liczb:", c, "-", d, "=", c-d)
else:
    print("Wybór został źle określony")
