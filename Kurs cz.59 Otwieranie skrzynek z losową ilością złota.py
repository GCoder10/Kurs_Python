'''
    Listy - zachowanie kolejności. Dużo możliwości operowania na danych, dlatego
    zajmują aż można powiedzieć najwięcej miejsca w pamięci. []

    
    Zbiór - operacje na zbiorach, suma, elementy wspólne, suma zbiorów, zbiór A
    minus zbiór B, czy zbiór A jest podzbiorem B. Idealne do testowania /
    porównywania danych między np. serwerami.
    Właściwość zbioru: elementy powtarzające się zostaną przerobione na unikalne.
    {}
    Elementy są wrzucane do "worka" bez zachowania ich kolejności.

    
    Słownik - KLUCZ: wartość - idealne do najszybszego odnajdowania danych
    po kluczu, nie trzeba stosować pętli przechodzącej po całym obiekcie
    słownikowym.
    {KLUCZ: wartość}

    
    Krotki - () lub bez - brak możliwości modyfikacji elementów. Najszybsze
    z reszty nad tym. Python rezerwuje tylko tyle miejsca, ile trzeba, brak
    funkcji / metod operowania na danych, usuwania, dodawania itp.

    
    Generatory - idealne do wielo terabajtowych danych, mamy dostęp do
    wygenerowanego elementu tylko w tym jednym momencie, nie możemy wracać
    do wcześniej wygenerowanych elementów. Można np. wyświetlić lub przekazać
    gdzieś indziej co chcemy, bo potem nie będzie odwołania do elementu.
'''
# ============================================================================
"""
    5 ruchów w jedną stronę poprzez komnatę.
    Za każdym ruchem jest szansa na napotkanie skrzynki lub niczego.
    Skrzynki mają różne kolory.

    Kolor skrzynki = jej rzadkość:
        zielona - 75%
        pomarańczowa - 20%
        fioletowa - 4%
        złota (legendarna) - 1%

        40% szansy na napotkanie niczego. 60% szansy na skrzynkę

    Złoto jako element mogący wypaść ze skrzynki:
        zielony - 1000,
        pomarańczowy - 4000,
        fioletowy - 9000,
        złota - 16000


    Pamiętać o:
    1) Czysty kod
    2) Samoopisujące się zmienne
    3) Program po angielsku
"""
import random
from enum import Enum

# ========================================================================
# Ustawienia, reszta automatycznie się dopasuje.
Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }

eventList = list(eventDictionary.keys()) # Lista na podstawie kluczy
eventProbability = list(eventDictionary.values()) # Lista na podstawie wartości

# Dzięki takiemu słownikowi, kod po angielsku ale program po polsku
Colours = Enum('Colours', {
                            'Green': 'zielony',
                            'Orange': 'pomarańczowy',
                            'Purple': 'fiolet',
                            'Gold': 'złoty'
                          })

'''
    Prawdopodobieństwa wystąpienia danych kolorów skrzynek
    chestColourList i chestColourProbability będzie potem używane do
    wygenerowania, co się akurat trafiło podczas gry.
    tuple - krotka
    krotka - nie zmienimy wartości w trakcie.
    chestColourList # Krotka na podstawie kluczy
    chestColourProbability # Krotka na podstawie wartości
'''
chestColoursDictionary = {
                            Colours.Green: 0.75,
                            Colours.Orange: 0.2,
                            Colours.Purple: 0.04,
                            Colours.Gold: 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

# Wyrażenie słownikowe. len = 4, range(4), 0 1 2 3
# Przydatne jak byłoby np. 100 nagród z jakąś zależnością matematyczną jak tutaj.
'''
    chestColourList[reward]: --> Colours.Green
    i dla klucza Colours.Green przypisanie wartości for reward in range(len(chestColourList)),
    jaka nagroda za dany kolor skrzynki.
    (reward + 1) * (reward + 1) * 1000 --> wartości do kolorów skrzynek.
    1000
    2*2 = 4 * 1000 = 4000
    3*3 = 9 * 1000 = 9000
    4*4 = 16 * 1000 = 16000

    for reward in range(len(chestColourList)) --> określenie, ile tych skrzynek, czyli nagród
    jest do ustalenia.
'''
rewardsForChests = {
                        chestColourList[reward]: (reward + 1) * (reward + 1) * 1000# Klucz
                        for reward in range(len(chestColourList)) # Co wybieramy, wartości
                   }

gameLength = 5

goldAcquired = 0
# ========================================================================
print("Welcome.")
print("You have only 5 steps to make.")

while gameLength > 0:
    gameAnswer = input("Do you want to move forward?")
    if (gameAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList, eventProbability)
        print("drawnEvent: ")
        print(drawnEvent)
        # Uzyskanie ostatecznie samej listy, pierwszy element:
        # drawnEvent2 - lista
        # Event.Chest - pojedyńczy element. [0], aby się do niego dostać
        drawnEvent2 = random.choices(eventList, eventProbability)[0]
        print("\n\n drawnEvent2: ")
        print(drawnEvent2)


        if (drawnEvent2 == Event.Chest):
            print("You have drawn a chest")
            drawnColour = random.choices(chestColourList, chestColourProbability)[0]
            print("The chest color is", drawnColour.value)
            gamerReward = rewardsForChests[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif(drawnEvent2 == Event.Empty):
            print("You have drawn nothing")
    else:
        print("You can go just straight man, nothing else.")
        continue
    
    gameLength -= 1

print("You have acquired: ", goldAcquired)
