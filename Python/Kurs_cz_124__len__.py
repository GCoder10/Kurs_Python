'''
    
'''
from __future__ import annotations
from random import randint
from math import sqrt


class Rocket:
    def __init__(self, speed:float = 1, altitude:float = 0, x:float = 0):
        self.altitude = altitude
        self.speed = speed
        self.x = x
    def moveUp(self):
        self.altitude += self.speed
    def __str__(self):
        # Podawanie informacji, gdy odwołamy się do obiektu jako string
        return "Zamiast informacji typu string o adresie obiektu, to coś innego. Wysokość: " + str(self.altitude)
    def get_distance(self, rocket: "Rocket"):
        return abs(rocket.altitude - self.altitude) # abs - wartość bezwzględna, absolute value
rocket1 = Rocket()

class RocketBoard:
    def __init__(self, amountOfRockets:int = 5):    
        #============================================
        # Wyrażenie listowe 
        print("Wyrażenie listowe")

        self.rockets = [
            Rocket() for _ in range(amountOfRockets) # _ <- zmienna nigdzie nie jest używana
        ]

        print(self.rockets)

        for _ in range(10): # 10 poruszeń losowych rakiet, 5 rakiet, więc: randint(0,4)
            rocketIndexToMove = randint(0,amountOfRockets - 1)
            self.rockets[rocketIndexToMove].moveUp()



        print("Zmienione wysokości:")
        for rocket in self.rockets:
            print(rocket.altitude)


        print("Adresy obiektów rocket :")
        for rocket in self.rockets:
            print(rocket)
        #=================end__init__==============
    def __getitem__(self, key):
        return self.rockets[key]
    def __setitem__(self, key, value):
        self.rockets[key].altitude = value
    def __len__(self):
        return len(self.rockets)
        # return self.get_amount_of_rockets()
    def get_amount_of_rockets(self):
        return len(self.rockets)
    @staticmethod
    def get_distance_via_pattern(rocket1: Rocket, rocket2: Rocket) -> float:
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)



#============================================
# Lista + pętla
print("Lista + pętla")

rockets = list()

for i in range(5):
    newRocket = Rocket()
    rockets.append(newRocket)

print(rockets)