"""
    czy:     el. unikalne   |   kolejność   |   zmiana konkretnego el.    |    nowe elementy
listy             NIE               TAK                   TAK                       TAK

krotki            NIE               TAK                   NIE                       NIE

słowniki          TAK               NIE                   TAK                       TAK

zbiory            TAK               NIE                   NIE                       TAK


ZBIORY: BONUS w postaci | & - ^
"""
# listy []
# krotki bez nawiasów lub ()
# słownik {}
'''
    Listy podobnie jak kontenery (vector) w C++11, kompilator w takim przypadku
    rezerwuje trochę więcej miejsca niż jest to potrzebne
    vector - praktycznie 2x więcej
    Listy, jest to związane z faktem, iż na listach można wykonywać wiele operacji
    dotyczących modyfikacji ich zawartości.

    
    Krotki - o wiele mniej miejsca w pamięci trzeba dla nich zarezerwować, co wiąże się
    bezpośrednio z faktem, iż działają one o wiele szybciej niż listy.
    Nie można modyfikować ich zawartości w trakcie działania programu.


    Słownik - KLUCZ: wartość. Kluczem może być wartość liczbowa ale także string.
'''


# Zbiór nie pozwala na wiele takich samych elementów
ZbiorA = {1, 4, 20, -4, 20}
print(ZbiorA)
# Nie da się indeksować:
# ZbiorA[2] = 4 --> Błąd



'''
    Dodanie elementu do zbioru
    Elementów w zbiorze nie da się indeksować, w trakcie pracy programu
    (podczas jego kompilacji) pozycje elementów mogą się zmienić / zostać
    automatycznie posortowane, zbiory także nie pozwalają na trzymanie wielu
    takich samych elementów.
'''
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Dodanie elementu do zbioru ZbiorA.add(7): ")
ZbiorA.add(7)
print(ZbiorA)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Dodanie elementu do zbioru takiego samego ZbiorA.add(7): ")
ZbiorA.add(7)
print(ZbiorA)



"""
    Można przetworzyć listę na zbiór w celu uzyskania samych unikalnych elementów,
    bez powtórek.
    Usuwanie duplikatów
"""
lista = [-9, -100, 23, 50, 61, -100, -9, 0, 1, 1]
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Lista: ")
print(lista)
print("Lista zamieniona w zbiór, funkcja set: ")
print(set(lista))




"""
    Zbiory można sumować itd.
    | & - ^
    Np. sprawdzanie, czy w dwóch bazach istnieją tacy sami użytkownicy.
    Suma dwóch zbiorów - wszystkie elementy z dwóch zbiorów będą unikalne.
"""
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
lista2 = [-80, 50, 25, 0, 0, 0, 1, 2, 1, 55, -100]
print("Lista: ")
print(lista)
print("Lista2: ")
print(lista2)
print("Wspólne elementy dwóch list pierw zamienionych na zbiory (funkcja set): ")
print(set(lista)&set(lista2))
print("Wszystkie elementy dwóch list pierw zamienionych na zbiory (funkcja set): ")
print(set(lista)|set(lista2))
print("Odjęcie elementów zbioru 2 od zbioru 1: ")
print(set(lista)-set(lista2))
print("XOR, alternatywa wykluczająca, suma elementów zbiorów minus część wspólna: ")
print(set(lista)^set(lista2))


"""
    Usuwanie elementów ze zbiorów
"""
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Usunięcie 0 ze zbioru: ")
print("Lista2: ")
print(set(lista2))
lista3 = set(lista2)
lista3.discard(0)
print("Lista3 bez 0: ")
print(lista3)




print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Usunięcie -80 ze zbioru: ")
print("Lista3: ")
print(lista3)
lista3.remove(-80)
print("Lista3 bez -80: ")
print(lista3)





"""
    Sprawdzanie, czy jeden zbiór jest podzbiorem innego zbioru
    False - nie jest
    Czyli, wszystkie elementy zbioru A muszą być w zbiorze B, aby powiedzieć, że
    zbiór A jest podzbiorem zbioru B
"""
lista4 = set(lista)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Lista3: ")
print(lista3)
print("Lista4: ")
print(lista4)
print("Sprawdzenie, czy zbiór lista3 jest podzbiorem listy4: ")
print(lista3.issubset(lista4))
lista5 = {0, 1, 2}
print(lista5.issubset(lista2))
