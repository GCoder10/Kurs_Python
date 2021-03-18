# len() - długość - length
# .append - dodać
# .extend - rozszerzyć
# .insert(index, co) - wstawić
# .index - indeks danego elementu
# sort(reverse = False) - sortuj rosnąco
# max()
# min()
# .count - ile razy coś wystąpi
# .pop - usuń ostatni element
# .remove - usuń pierwsze wystąpienie
# .clear - wyczyść listę
# .reverse - zamień kolejność

lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]
lista3 = [54, 1, -2, 20, 1, 0, -30, 504, 4, 1]

print("# len() - długość - length: 5")
print(len(lista1))

print("# len() - długość - length: 2")
print(len(lista2))


print(".append - dodać. Dodawanie elementów do końca listy: ")
print("[54, 1, -2, 20, 1, 4] ")
lista1.append(4)
print(lista1)


'''
    lista1.append(4) <-- Dodaje do końca listy
    lista1 + [4]     <-- Nie zmienia zawartości listy
    lista1 = lista1 + [4] <-- Podmiana zawartości listy1, dużo wolniejsze od
                              użycia append

    .extend jest też oczywiście o wiele szybsze niż +
'''
print(".extend - rozszerzyć. Dodawanie elementów do końca listy: ")
print("[54, 1, -2, 20, 1, 4, 2, 12, 24, 2] ")
lista1.extend([2, 12, 24, 2])
print(lista1)



print(".append dodaje jako jeden element: ")
print("Lista w liście ")
print("[54, 1, -2, 20, 1, 4, 2, 12, 24, 2, [2, -2, 100]] ")
lista1.append([2, -2, 100])
print(lista1)



"""
    # .insert(index, co) - wstawić
"""
print(".insert - wstawianie do listy na określoną pozycję: ")
print("")
print('["Kuba", "Arkadiusz", "Wioletta"] ')
lista2.insert(0, "Kuba")
print(lista2)




print(".insert - wstawianie do listy na określoną pozycję: ")
print("")
print('["Kuba", "Arkadiusz", "Jakub", "Wioletta"] ')
lista2.insert(2, "Jakub")
print(lista2)


"""
   # .index - indeks danego elementu
   Jeżeli jest wiele elementów takich samych, to index zwraca indeks pierwszego
   wystąpienia szukanego elementu.
"""
print("")
print("")
print("")
print(".index - indeks danego elementu: ")
print('["Kuba", "Arkadiusz", "Jakub", "Wioletta"]: "Wioletta": 3 ')
print(lista2)
print(lista2.index("Wioletta"))




"""
    # sort(reverse = False) - sortuj rosnąco
    Funkcja sort zmienia zawartość, na posortowaną
    Domyślne sortowanie - rosnąco
    lista3.sort(reverse = True) - malejąco
"""
print("")
print("")
print("")
print(".sort (rosnąco): ")
print('')
print(lista3)
lista3.sort()
print(lista3)


print("")
print("")
print("")
print(".sort (malejąco): ")
print('')
print(lista3)
lista3.sort(reverse = True)
print(lista3)



print("")
print("")
print("")
print(".sort (rosnąco): ")
print('')
print(lista2)
lista2.sort()
print(lista2)


print("")
print("")
print("")
print(".sort (malejąco): ")
print('')
print(lista2)
lista2.sort(reverse = True)
print(lista2)


"""
    # max() - znajdywanie maksymalnej wartości
"""
print("")
print("")
print("")
print(".max() - 504: ")
print('')
print(lista3)
print(max(lista3))





"""
    # min() - znajdywanie minimalnej wartości
"""
print("")
print("")
print("")
print(".min() - (-30): ")
print('')
print(lista3)
print(min(lista3))



"""
    # .count - ile razy coś wystąpi
"""
print("")
print("")
print("")
print(".count(1) - 3: ")
print('')
print(lista3)
print(lista3.count(1))


"""
    # .pop - usuń ostatni element
"""
print("")
print("")
print("")
print(".pop(): ")
print('Przed: ')
print(lista3)
lista3.pop()
print('Po: ')
print(lista3)




"""
    # .remove - usuń pierwsze wystąpienie
"""
print("")
print("")
print("")
print(".remove(1): ")
print('Przed: ')
print(lista3)
lista3.remove(1)
print('Po: ')
print(lista3)



"""
    # .clear - wyczyść listę
"""
print("")
print("")
print("")
print(".clear(): ")
print('Przed: ')
print(lista1)
lista1.clear()
print('Po: ')
print(lista1)




"""
    # .reverse - zamień kolejność
"""
print("")
print("")
print("")
print(".reverse(): ")
print('Przed: ')
print(lista3)
lista3.reverse()
print('Po: ')
print(lista3)
