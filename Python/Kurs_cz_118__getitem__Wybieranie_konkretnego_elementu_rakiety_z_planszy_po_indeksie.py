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

class RocketBoard:
    def __init__(self, amountOfRockets = 5):    
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



#============================================
# Lista + pętla
print("Lista + pętla")

rockets = list()

for i in range(5):
    newRocket = Rocket()
    rockets.append(newRocket)

print(rockets)