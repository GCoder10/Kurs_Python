wartosc = int(input("Sprawdzenie, czy liczba jest z zakresu 1 - 10: "))

if ((wartosc > 1) and (wartosc < 10)):
    print("Wartość jest z zakresu 1 - 10")


a = 5
b = 2

if (a == 5 or b == 3):
    print("tak")


# Operatory logiczne, operacje na bitach są o wiele szybsze od
# standardowych operacji arytmetycznych z perspektywy kompilatora,
# komputera.

"""
    OPERATORY LOGICZNE:
        and - wszystkie wyrażenia muszą dać PRAWDĘ (&&) - koniunkcja
        or  - lub - (||) - chociaż jedno wyrażenie musi dać PRAWDĘ - alternatywa
        not - nie - zaprzecza, jak ! w innych językach
"""


if (a == 5 and b == 3):
    print("tak and bez not")



if (not(a == 5 and b == 3)):
    print("tak and z not")
