liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = [] # Tworzenie nowej listy na podstawie starej listy
for element in liczby:
    potegiDwojki.append(element**2) # .append() - dodaj na sam koniec


liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)


'''
    A zrobienie nowej listy na podstawie starej można też inaczej, czyli
    wyrażenie listowe.

    Podejście wyrażeniem listowym jest o wiele szybsze od używania
    append z uwagi na fakt istnienia różnic optymalizacyjnych.
'''
potegiDwojki2 = [element**2             # <-- formuła
                 for element in liczby] # <-- formuła
print(potegiDwojki2)


liczbyParzyste2 = [element                # <-- formuła
                   for element in liczby  # <-- formuła
                   if (element % 2 == 0)] # <-- formuła
print(liczbyParzyste2)


potegiDwojki3 = [element**2                # <-- formuła
                 for element in range(20)] # <-- formuła
print(potegiDwojki3)
