"""
    Wyrażenie zbioru
"""

# Zbiór
names = {"Arkadiusz", "Wioletta", "karol", "bartłomiej", "jakub", "Ania"}

names = {
    name.capitalize()
    for name in names
}

print("Zamiana elementów z jednego zbioru na drugi zbiór. Pierwsza litera imienia jako duża: ")
print(names)


