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
    read
    readline - czyta pojedynczą linię
    readlines - czyta wszystkie linie i wrzuca w listę, tyle że zachowuje \n

    splitlines - zwraca ostatecznie liste wszystkich elementów bez \n
'''
with open("oceany.txt", encoding = "UTF-8") as file: #Uchwyt File, Obiekt file
    # Obiekt file ma inne kodowanie znaków niż dane w pliku txt
    # Mogą wtedy pojawiać się pewne nieprawidłowości w odczycie tylko z
    # uwagi na fakt różnego kodowania znaków w plikach
    # Oryginalnie kodowanie w obiekcie file było: cp1250
    oceany = file.read().splitlines()
    print("Z listą: ")
    print(oceany) # Funkcja print odczytuje z \n prawidłowo
    print("oceany[0]: ")
    print(oceany[0])
    print("file.encoding: ")
    print(file.encoding)


with open("oceany.txt", encoding = "UTF-8") as file2:
    oceany = file2.readline() # Pierwsza linia i operacje na niej
    print("[1] Oceany readline(): ")
    print(oceany)
    print("oceany[0]: ")
    print(oceany[0])
    oceany2 = file2.readline() # Druga linia i operacje na niej
    print("[2] Oceany2 readline(): ")
    print(oceany2)
    print("oceany2[0]: ")
    print(oceany2[0])


with open("oceany.txt", encoding = "UTF-8") as file3:
    oceany3 = file3.readlines() 
    print("Oceany readlines(): ")
    print(oceany3)


with open("oceany.txt", encoding = "UTF-8") as file4:
    print("for line in file4: ")
    for line in file4:
        print(line)
