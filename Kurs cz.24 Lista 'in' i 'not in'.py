# in
# not in
# Operacje na listach

lista_imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian", "Wojtek"]
liczby = [1, 54, -2, 20]
liczby2 = [3, 12, 24, 7, -8]

'''
    Szukanie, czy dany element znajduje się w liście.
    W innych językach normalnie stosuje się pętle i gdy znajdzie się tylko
    dany element, to np. break do przerwania pracy pętli.
    Python - in
'''
print("Arkadiusz" in lista_imiona) # Zwraca True/False. True, jest w liście.

print("Jakub" in lista_imiona) # False, nie ma w liście.
"""
    Za funkcjonalnością in kryje się funkcja predefiniowana wykonująca to, co
    zostało opisane w zielonym komentarzu powyżej.
    Funkcja zwracająca typ bool.
"""
print("Przykład wykorzystania funkcji in: ")
if ("Kuba" in lista_imiona):
    print("Cześć Jakubie")


'''
    not in - funkcja zwracająca True, jeżeli nie ma w liście szukanego
    elementu.
'''
print("Not in: ")
if (2 not in liczby):
    print("Nie ma liczby 2")



print("Not in (element jednak jest w liście): ")
if (54 not in liczby):
    print("Nie ma liczby 54")
else:
    print("Liczba 54 znajduje się w przeszukiwanej liście")


"""
    Inny zapis dla funkcji not in
"""
print("not 2 in: ")
if (not 2 in liczby):
    print("Nie ma liczby 2")
else:
    print("Liczba 2 znajduje się w przeszukiwanej liście")


'''
    Operacje na listach
    4 + liczby2 = nie da się.
'''
print("Operacje na listach - 3 *: ")
print(3 * liczby2)


print("Operacje na listach + [4]: ")
print("Dwie listy łączymy w jedną: ")
print([4] + liczby2)



print("Operacje na listach + [4, 20, 15]: ")
print("Dwie listy łączymy w jedną: ")
print([4, 20, 15] + liczby2)

print("Nie łączymy w ten sposób list na zawsze: ")
print(liczby2)




print("Podmiana na zawsze: ")
liczby2 = [4, 20, 15] + liczby2
print("liczby2 = [4, 20, 15] + liczby2")
print(liczby2)
