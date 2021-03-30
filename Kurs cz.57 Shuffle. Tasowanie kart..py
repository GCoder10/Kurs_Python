"""
    Shuffle - randomizes entire list
    Przetasować
    Zmienia kolejność jakiegoś zbioru elementów.
    Funkcja działająca na oryginale.
    Obiekty - listy, zbiory, itd. są mutable - zmienne, więc dlatego
    funkcja działa na oryginale.
    Niezmienne - immutable - są obiekty takie jak: int, double, float itp.
"""
import random

cardList = [    "9",     "9",     "9",     "9",
               "10",    "10",    "10",    "10",
             "Jack",  "Jack",  "Jack",  "Jack",
            "Queen", "Queen", "Queen", "Queen",
             "King",  "King",  "King",  "King",
              "Ace",   "Ace",   "Ace",   "Ace",
            "Joker", "Joker"]

print(cardList)

random.shuffle(cardList)

print(cardList)
