'''
    docstring -- DOCument string.
    Dokumentowanie klas.
    Komentarze też mogą do tego posłużyć.
    VSC -> Extensions -> Python Docstring Generator by Nils Werner

    Piszemy """ i ENTER = automatyczne utworzenie docstring dla
    klasy/metody itd. przez plugin.
'''
from random import randint


class Rocket: # speed wart. domyślna, gdyby nic nie zostało przesłane podczas inicjalizacji klasy poprzez użycie obiektu.
    """
        Miejsce na docstring
        Pojawi się wyjątkowo w miejscu.
        Gdy piszemy rocket = Rocket(), jako podpowiedź w VSC
        się pojawi informacja zapisana tutaj, opis tej klasy.
    """

    def __init__(self, speed = 1):
        """[Utworzone przez plugin]

        Args:
            speed (int, optional): [description]. Defaults to 1.
        """
      self.altitude = 0
      self.speed = speed
    def moveUp(self):
        """
            docstring dla metody
            rocket.moveUp() w VSC pojawi się podpowiedź w postaci
            informacji o tej metodzie w tej klasie.
        """
        self.altitude += self.speed
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


rockets1[0].moveUp()
rockets1[1].moveUp()
rockets1[2].moveUp()
rockets1[2].moveUp()

# rocket = Rocket()
# rocket.moveUp()