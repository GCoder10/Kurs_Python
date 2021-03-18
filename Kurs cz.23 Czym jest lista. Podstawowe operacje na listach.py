# Czym są listy
    #- trochę jak tablica, przechowywanie wartości elementów
# Jak je tworzyć

# Jak zmieniać wartości
# Jak wypisywać wartości
# Jak wypisywać wszystkie wartości
# Po co są listy

lista_imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian"] # 5 elementów
liczby = [1, 54, -2, 20]
lista_mieszana = [1, "aa", 52, "k"]

print("Wszystkie imiona z listy: ")
print(lista_imiona)

print("Wszystkie imiona z listy - pętla for: ")
for imie in lista_imiona:
    print(imie)


"""
    Elementy w liście, tak samo jak w tablicach czy też kontenerach (C++11 STL) są
    indeksowane od zera.
"""

print("1-wsze imie: ")
print(lista_imiona[0])


print("5-te imie: ")
print(lista_imiona[4])


"""
    Python umożliwia poruszanie się od końca dzięki ujemnych indeksom
"""
print("Ostatni element indeks -1: ")
print(lista_mieszana[-1])

print("Przedostatni element indeks -2: ")
print(lista_mieszana[-2])


print("Podmiana elementów w liście: ")
lista_mieszana[-3] = "CośNowegoPodmiana"
print(lista_mieszana[1])
