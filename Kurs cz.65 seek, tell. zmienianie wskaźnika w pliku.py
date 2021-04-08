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
    tell - mówi, gdzie skończyliśmy ostatnią operacje na pliku
    seek - szuka (zmienia) - na miejsce wskazane przez nas
'''
with open("oceany.txt", "r", encoding = "UTF-8") as file: 
    print(file.read()) # Czyli wskaźnik odczytu znajduje się na samym końcu
    # pliku. Trzeba by było znowu otwierać plik, aby go odczytać od początku.
    print(file.read())


with open("oceany.txt", "r", encoding = "UTF-8") as file: 
    print(file.readline())
    print("Wskaźnik odczytu tell(): ")
    print(file.tell())
    print(file.readline())
    print("Wskaźnik odczytu tell(): ") # \n liczy jako dwa znaki
    print(file.tell())
    
    file.seek(0)
    print(file.readline())
    print("Wskaźnik odczytu tell() po ustawieniu go na seek(0): ")
    print(file.tell())

    file.seek(4)
    print(file.readline())
    print("Wskaźnik odczytu tell() po ustawieniu go na seek(4): ")
    print(file.tell())
