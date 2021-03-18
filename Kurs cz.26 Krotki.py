# Krotka
"""
    Krotka też służy do przechowywania elementów.
    Elementy zapisane do krotki na starcie nie będzie można później
    już zmienić.
"""
# Krotka a lista
"""
    Powinno się korzystać z krotki zawsze, gdy tylko można.
    Jeżeli wewnątrz programu / projektu będą takie elementy, których nie
    powinno się zmieniać w trakcie działania programu lub nie ma takiego
    logicznego uzasadnienia.

    Krotka - rezerwacja określonego miejsca w pamięci. Będzie ona szybsza
    nawet kilkukrotnie przy dużych ilościach danych.
    Kompilator z góry wie, ile miejsca trzeba zarezerwować i że na przyszłość
    tylko tyle miejsca wystarczy.
"""
# Python, listy, rezerwacja pamięci
"""
    Kompilator rezerwuje dla listy trochę więcej miejsca w pamięci, niż
    aktualnie jest potrzebne.
    Ma to ścisły związek z faktem, iż w późniejszych etapach działania
    programu można wpływać na elementy z listy.
    Trochę jak vector, kontener w C++11, tyle że tam następuje rezerwacja
    aż dwukrotnie większej ilości pamięci niż aktualnie jest używana.
"""
lista = [1, 42, 12, -4]
krotka = 1, 42, 12, -4
krotka2 = (1, 42, 12, -4)

print("krotka[0]: ")
print(krotka[0])


print("krotka2[0]: ")
print(krotka2[0])



# krotka[0] = 4 <-- Błąd
lista[0] = 4 # OK


