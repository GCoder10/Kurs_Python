"""
import random

    random - losowy
    random()               0 <= x < 1 lub [0, 1)
    uniform(2.5, 10.0)     2.5 <= x < 10.0 lub [2.5, 10)
    randrange(10)          z puli (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    randrange(0, 15, 2)    parzyste z puli (0, 2, 4 ... 14)

    randint(0, 4) [0,4]
"""
import random

x = 0
while x < 100:
    x = x + 1
    print(x)
    print("random.random()")
    print(random.random())
    print("\n\n\n")



x = 0
while x < 100:
    x = x + 1
    print(x)
    print("random.uniform(0, 100)")
    print(random.uniform(0, 100))
    print("\n\n\n")

def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


print(will_weapon_hit(50)) # Co drugi raz powinien trafić teoretycznie


'''
    Funkcja licząca szanse na trafienie, jeżeli podamy argument 100 to
    zawsze będą trafienia (isHitChance będzie zawsze mniejsze tutaj od 100)
    Wyniki trafień zapisywane do listy.

    listHit.count('hit') -- zliczenie wszystkich trafień przechowywanych w
    liście.
'''
x = 0
listHit = []
while x < 100:
    x += 1
    listHit.append(will_weapon_hit(50))
    

print("listHit: ")
print(listHit)

print("listHit.count('hit'): ")
print(listHit.count("hit"))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

"""
    Automatyczne liczenie wszystkich powtarzających się poszczególnych
    elementów w przekazywanej liście i zapisanie wyniku
    jako słownik.

    KLUCZ: element
    wartość: ilość powtórzeń
"""
from collections import Counter

dictionaryHit = Counter(listHit)
print("dictionaryHit: ")
print(dictionaryHit)


print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

'''
    ========================================================================
'''
x = 0
while x < 100:
    x += 1
    print("random.randrange(10): ")
    print(random.randrange(10))


'''
    ========================================================================
'''
x = 0
while x < 100:
    x += 1
    print("random.randint(0, 10): ")
    print(random.randint(0, 10))
