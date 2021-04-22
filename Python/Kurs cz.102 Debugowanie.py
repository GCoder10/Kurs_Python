"""

"""
from collections import Counter
import random


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)

    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


x = 0

listHit = []
#weaponHitPercentage = input("Podaj szanse na uderzenie broni")
while x < 5:
    x = x + 1
    listHit.append(will_weapon_hit(50))


dictionaryHit = Counter(listHit)

print(listHit)