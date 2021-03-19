"""
Program:
    1). Dodawanie nowych definicji.
    2). Szukanie istniejących definicji.
    3). Usuwanie wybranej definicji.
"""
definicje = {}


while(True):
    print("1. Dodaj definicje.")
    print("2. Znajdź definicje.")
    print("3. Usuń definicje.")
    print("4. Zakończ program.")

    wybor = input("Co chcesz zrobić? ") # Brak rzutowania. Input -> char, tutaj char wystarczy.

    if (wybor == '1'):
        klucz = input("Podaj klucz (słowo do zdefiniowania): ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif (wybor == '2'):
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif (wybor == '3'):
        klucz = input("Jaką definicję chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunięto definicję o nazwie:", klucz)
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif (wybor == '4'):
        print("Program kończy pracę.")
        break
    else:
        print("Podałeś opcję z poza zakresu")
