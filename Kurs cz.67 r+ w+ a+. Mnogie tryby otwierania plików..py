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
   mnogie tryby otwierania plików:
   r+ - do czytania i pisania
   file.read
   file.write
   Trzeba pamiętać o dostosowywaniu wskaźnika.

   w+ - do pisania i czytania.
   różni się tym, że usunie zawartość istniejącego pliku lub stworzy plik
   gdy go nie było.

   a+ - "wieczny tryb" dopisywania i czytania
   Wskaźnik dopisywania jest zawsze na końcu, jeśli plik nie istniał - stworzy go
'''
with open("oceany.txt", "r+", encoding = "UTF-8") as file:
    file.readline() # Jeżeli nie ma takiego pliku, to błąd, nie usuwa, jeśli
    # istnieje.

with open("oceanyNieIstniały.txt", "w+", encoding = "UTF-8") as file:
    file.readline() # Jeżeli plik nie istniał, to go stworzy.


with open("oceany2.txt", "w+", encoding = "UTF-8") as file:
    file.readline() # Jeżeli plik istniał, to usunie jego zawartość.

with open("oceany.txt", "a+", encoding = "UTF-8") as file:
    print("Tryb a+, tell(): ")
    print(file.tell())
    file.write("\nNowy Ocełannn")
    print("tell(): ")
    print(file.tell())
    file.seek(0)
    print("seek(0): ")
    print(file.tell())
    print("file.readline(): ")
    print(file.readline())
    print("Dopisze i tak na samym końcu pomimo, że wskaźnik nie jest na końcu: ")
    file.write("\n i tak na końcu")
    print("Po dopisaniu tell(): ")
    print(file.tell())
