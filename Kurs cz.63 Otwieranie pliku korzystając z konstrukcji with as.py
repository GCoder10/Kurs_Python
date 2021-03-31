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
    with otwarty plik / flagi jako plik i instrukcje operacji na tym otwartym pliku.
    Dzięki with as plik zawsze zostanie automatycznie zamknięty, nawet jeżeli po
    drodze wystąpi jakiś błąd.
'''

with open("test4.txt", "w") as file: # file - Handle
    file.write("Sample \n")
    print(0/0)
    tab = [1,2]
    print(tab[4])
    file.write("Sample222")
