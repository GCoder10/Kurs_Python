import math

imie = "przykładoweImie"
print(imie)

imie.capitalize() # Funkcja wbudowana. import string. 1-wsza duża, reszta małe

print(imie.capitalize()) # Zmiana na kopii zmiennej imie
"""
    Funkcje w większości przypadków przy takim zastosowaniu jak wyżej
    działają na kopii zmiennych.
"""
print(imie)

imie2 = imie.capitalize()

print(imie2)


'''
    Funkcja upper() powiększa wszystkie litery
'''
print(imie.upper())



'''
    Funkcja lower() zmniejsza wszystkie litery
'''
print(imie.lower())



imie2 = imie.lower()
print(imie2)

'''
    math
'''
print(math.sqrt(4))
