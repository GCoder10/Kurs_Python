"""
    PLIK - nazwana lokacja, która przechowuje na stałe dane na dysku.

    RAM - pamięć podręczna komputera, gdzie przechowywane są dane tymczasowo.

    Operacje na plikach:
    1) Otwieranie
    2) Pisanie / czytanie
    3) Zamykanie

    Podstawowe sposoby otwierania plików:
    r - Read (czytanie) - domyślne
    w - Write (pisanie) - jeżeli plik istniał to go usunie, jeżeli nie to stworzy
    a - Append (dopisywanie)

    rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy rozpoznawały plik w
    odpowiedni dla tych programów sposób
"""
'''
    try: spróbuj zrobić
    finally: rób zawsze po try, nawet jeżeli wystąpią tam błędy.
'''
try:
    # Plik przechowywany w obiekcie file. File jest teraz uchwytem, handle
    file = open("test4.txt", "w")
    file.write("Sample \n")
    print(0/0)
    tab = [1,2]
    print(tab[4])
    file.write("Sample222")
finally:
    file.close() # Zwolnienie pamięci, podobnie jak w C/C++/C++11 dla kontenerów, pamięci dynamicznie
    # alokowanych przy pomocy np. new int.
    
