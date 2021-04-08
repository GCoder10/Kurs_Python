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
    
'''
with open("oceany.txt", "a", encoding = "UTF-8") as file:
    print("Append - wskaźnik będzie od razu na końcu pliku: ")
    print(file.tell())
    file.write("\nPołudniowy 2")
