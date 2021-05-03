from Kurs_cz_119__setitem__Zmiana_wartosci_konkretnego_elementu_rakiety_z_planszy_po_indeksie import Rocket, RocketBoard
from random import randint
'''
    Import dwóch klas z innego pliku.
    Zdefiniowanie klas w innym pliku, zaimportowanie ich i dopiero
    kodowanie z otwartym drugim plikiem z klasami.

'''

# Plansza z ruchem rakiet przy inicjalizacji (__init__)
# Plansza z n rakietami na start ze zmianą wysokości
# Klasa RocketBoard ma ustawioną domyślną ilość rakiet na 5, gdyby
# nie został przesłany parametr.
board = RocketBoard(15)


# board. <-- nie będzie do niczego dostępu, rakiety istniały
# lokalnie dopóki działał konstruktor, trochę logika jak z 
# generatorami, tam też dostęp do elementu jest tylko w momencie
# jego wygenerowania.
# trzeba w klasie RocketBoard dopisać przedrostek self przed rockets,
# wtedy dopiero będzie odwołanie do rakiet stworzonych w ramach obiektu 
# board, instancji klasy.

board.rockets[0].altitude = 40
print(board.rockets[0].altitude)

# Kolejna metoda dunder - double underscore __
# Metody wywołujące się w określonym momencie:
# __init__ podczas inicjalizacji klasy przy pomocy obiektu (jej instancji)
# __getitem__ podczas odwoływania się do obiektu przy pomocy nawiasów, klamer: object[index]
# __setitem__ podczas odwoływania się do object[index] z jednoczesnym przypisaniem nowej wartości.
# Jest konieczne zadeklarowanie tego w dunder method, żeby program 'wiedział', do czego przypisać tak
# napisaną wartość, bo przecież może być wiele atrybutów w danym obiekcie.
board[0].altitude = 79
print(board[0].altitude)

board[0] = 180
print(board[0].altitude)