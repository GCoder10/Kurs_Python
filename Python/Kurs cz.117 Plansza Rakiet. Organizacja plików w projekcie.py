'''
    
'''
from random import randint


class Rocket:
    def __init__(self, speed = 1):
        self.altitude = 0
        self.speed = speed
    def moveUp(self):
        self.altitude += self.speed
    def __str__(self):
        # Podawanie informacji, gdy odwołamy się do obiektu jako string
        return "Zamiast informacji typu string o adresie obiektu, to coś innego. Wysokość: " + str(self.altitude)
rocket1 = Rocket()



#============================================
# Lista + pętla
print("Lista + pętla")

rockets = list()

for i in range(5):
    newRocket = Rocket()
    rockets.append(newRocket)

print(rockets)

#============================================
# Wyrażenie listowe
print("Wyrażenie listowe")

rockets1 = [
    Rocket() for _ in range(5) # _ <- zmienna nigdzie nie jest używana
]

print(rockets1)

for _ in range(10): # 10 poruszeń losowych rakiet, 5 rakiet, więc: randint(0,4)
    rocketIndexToMove = randint(0,4)
    rockets1[rocketIndexToMove].moveUp()



print("Zmienione wysokości:")
for rocket in rockets1:
    print(rocket.altitude)

'''
rockets1[0].moveUp()
rockets1[1].moveUp()
rockets1[2].moveUp()
rockets1[2].moveUp()
'''


print("Adresy obiektów rocket :")
for rocket in rockets1:
    print(rocket)