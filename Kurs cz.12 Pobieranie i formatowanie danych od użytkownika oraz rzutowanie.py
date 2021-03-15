a = input() # Oczekiwanie na dane, traktuje jako ciąg znaków
b = input()
# a = 5, b = 10, a + b = '510'
print('Podaj c i d:')


"""
    Rzutowanie konieczne z ciągu znaków na coś innego
"""
print("Kalkulator do dodawania")
c = int(input("Podaj pierwszą liczbę: "))
d = int(input("Podaj drugą liczbę: "))
print("Wynik dodawania: " + str(c + d))
print("Wynik dodawania 2:", c + d) # , dodaje automatycznie spacje
print("Wynik dodawania 3. liczb:", c, "i", d, "wynosi:", c + d)
