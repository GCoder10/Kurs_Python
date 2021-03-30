"""
    choice  - zwraca losowy element
    Wylosowanie poszczególnego elementu jest takie samo dla wszystkich (szansa).
    
    choices - zwraca listę elementów i ma większe możliwości.
    Możemy ustalać prawdopodobieństwo wylosowania dla każdego elementu oddzielnie.
"""
import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

print("random.choice(movieList): ")
print(random.choice(movieList))



print("random.choices(nagrodaZeSkrzynki): ")
print(random.choices(nagrodaZeSkrzynki))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


'''
    ========================================================================
    k = 100 - Wylosowanie 100 razy. Zapisanie wyniku losowań do listy.
    Counter - Zapisanie do słownika ilości powtarzających się elementów
    z listy uzyskanej dzięki funkcji choices.
    KLUCZ - nazwa elementu
    wartość - ilość wystąpień
'''

print("random.choices(nagrodaZeSkrzynki, k = 100): ")
print(random.choices(nagrodaZeSkrzynki, k = 100))




from collections import Counter
print("Counter(random.choices(nagrodaZeSkrzynki, k = 100)): ")
print(Counter(random.choices(nagrodaZeSkrzynki, k = 100)))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


'''
    ========================================================================
    Ustalanie prawdopodobieństwa wystąpienia dla danego elementu z listy:
    [1, 2, 1, 2] - zielonego tak samo często jak purpurowej.
    pomarańczowa i legendarna dwa razy częściej od reszty.
    Tzw. średnia ważona
'''
print("Counter(random.choices(nagrodaZeSkrzynki, [1, 2, 1, 2], k = 100)): ")
print(Counter(random.choices(nagrodaZeSkrzynki, [1, 2, 1, 2], k = 100)))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


'''
    ========================================================================
    80% szansy na zielona
    15% szansy na pomarańczowa
    4%  szansy na purpurowa
    1%  szansy na legendarna
'''
print("Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 4, 1], k = 100)): ")
print(Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 4, 1], k = 100)))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



'''
    ========================================================================
    80% szansy na zielona
    15% szansy na pomarańczowa
    4%  szansy na purpurowa
    1%  szansy na legendarna
'''
print("Counter(random.choices(nagrodaZeSkrzynki, [0.8, 0.15, 0.04, 0.01], k = 100)): ")
print(Counter(random.choices(nagrodaZeSkrzynki, [0.8, 0.15, 0.04, 0.01], k = 100)))
