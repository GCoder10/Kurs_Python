"""
    Wyrażenia słownikowe -
    transformowanie dwóch skrajnie różnych obiektów przechowujących dane
    w programie (np. zbiór, lista) w słownik.
"""

# Zbiór
names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

# Lista
numbers = [1, 2, 3, 4, 5, 6]

# Słownik
celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

# Słownik, klucze to imiona
namesLength = {
    name : 2
    for name in names
}

print("Słownik, klucze to imiona: ")
print(namesLength)


# Klucz = imie, wartość = długość tego imienia.
namesLength = {
    name : len(name)
    for name in names
}

print("Klucz = imie, wartość = długość tego imienia: ")
print(namesLength)


namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

print("Tylko imiona zaczynające się na 'A': ")
print(namesLength)

multipliedNumbers = {
    number : number*number
    for number in numbers
}

print("Słownik. Przemnożone elementy przez siebie: ")
print(multipliedNumbers)

# Celcius
# Zmiana jednej wersji słownika na drugą
# C na F
'''
    items() zwraca listę krotek
'''
fahrenheit = {
    key: (celcius * 1.8) + 32
    for key, celcius in celcius.items()
}
print("C na F: ")
print(fahrenheit)



fahrenheit = {
    key: (celcius * 1.8) + 32
    for key, celcius in celcius.items()
    if celcius > -5
}
print("C na F, jeżeli C > -5 stopni: ")
print(fahrenheit)





fahrenheit = {
    key: (celcius * 1.8) + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}
print("C na F, jeżeli C > -5 stopni i jeżeli C < 20: ")
print(fahrenheit)


# Przemnożone liczby przez siebie.
multipliedNumbers = {
    number : number*number
    for number in range(1,70)
}
print("Słownik. Przemnożone elementy przez siebie. Od 1 do 70: ")
print(multipliedNumbers)
