wynik = 0 

'''
i = 0
while i < 4:
    x = int(input("Podaj liczbe: "))
    wynik += x
    i += 1
print("Wynik dodawania liczb to:",wynik)
'''



# Pętla for w Python nie potrzebuje pisania inkrementacji (POST,PRE) w
# ciele pętli.
# Funkcja range zwraca liste, zwraca np. [0,1,2]
"""
    for - dla każdego elementu z listy zwracanej przez funkcje range
    wykonaj (instrukcje w ciele pętli)
    Ile elementów w liście, tyle razy wykona sie cała pętla
"""
for i in range(0,4):
    x = int(input("Podaj liczbe: "))
    wynik += x
print("Wynik dodawania liczb to:",wynik)




wynik = 0
for i in [0,1]:
    x = int(input("Podaj liczbe: "))
    wynik += x
    print(i)
print("Wynik dodawania liczb to:",wynik)




"""
    W funkcji range jako parametr nie musimy podawać zakresu, można napisać
    od razu ilość razy jaką chcemy.
    Funkcja range przyjmuje od razy ilość razy bez zakresu to i tak zwróci
    odpowiednią listę, tutaj:
    [0,1,2,3,4,5,6,7,8,9]
"""
wynik = 0
for i in range(10):
    x = int(input("Podaj liczbe: "))
    wynik += x
    print(i)
print("Wynik dodawania liczb to:",wynik)



wynik = 0
"""
    Lista zwracana przez funkcję range nie musi posiadać poukładanych elementów,
    aby pętla wykonała się odpowiednią ilość razy.
    Liczy się ilość elementów w liście.
    Zamiast listy może to być także ciąg znaków.
"""
for i in [12,1000,300]:
    x = int(input("Podaj liczbe: "))
    wynik += x
    print(i)
print("Wynik dodawania liczb to:",wynik)




'''
    Zmienna i przechowuje stan aktualnego przejścia pętli:
    1. c
    2. z
    3. t
    4. e
    5. r
    6. y
'''
wynik = 0
for i in 'cztery':
    x = int(input("Podaj liczbe: "))
    wynik += x
    print(i)
print("Wynik dodawania liczb to:",wynik)




"""
    Wyłącznie parzyste liczby
    Liczba modulo 2 daje reszte 0, reszta z dzielenia danej liczby przez dwa
"""
for i in range(1200):
    if (i % 2 == 0):
        print("Liczba", i, "jest parzysta")
