"""
    Wczytanie imion i nazwisk z pliku:
    imionanazwiska.txt

    1). Rozdzielenie tak, aby powstała lista krotek, gdzie wewnętrzne krotki to
    pary imiona/nazwiska.

    2). Zapisanie imion do pliku imiona.txt

    3). Zapisanie nazwisk do pliku nazwiska.txt

    Nie ma podanego nazwiska w pliku imionanazwiska.txt, podczas zapisywania
    nazwiska do pliku nazwiska.txt
"""
'''
   [
        ("imie", "nazwisko"),
        ("imie2", "nazwisko2")
   ]

   Po każdym imieniu przed nazwiskiem jest spacja, czyli można rozdzielać
   po spacji.

   split(" "), rozdzielenie według wprowadzonego separatora, zwróci listę.

   Przerobienie listy na krotkę - tuple

   Usuwanie \n z końca linii - replace("\n", "")


   Dodawanie uzyskanych krotek do końca listy:
   namesAndSurnames.append(tuple(line.replace("\n", "").split(" ")))
    Uzyskano listę krotek na podstawie danych z pliku txt

=========================================================================
Dodawanie imion do pliku txt:

for item in namesAndSurnames:
       file.write(item[0] + "\n")

Każdy item to krotka w liście namesAndSurnames,
trzeba odwoływać się do [0], aby wczytać imie, [1] to nazwisko,
pętla for przejdzie przez wszystkie krotki w liście.
Dodanie na końcu nowej linii, aby imiona w pliku zostały wypisane
jedno pod drugim.

=========================================================================

Dodawanie nazwisk do pliku txt:
Błąd - brakuje jednego nazwiska, błąd o wyjściu poza zasięg krotki.
Dwa sposoby na poradzenie sobie z tym:
if(len(item) == 2):
sprawdzenie, czy krotka posiada dwa elementy (imie i nazwisko)
Dzięki temu imie bez nazwiska, nazwisko będzie puste, nowa linia.




Drugi sposób:
wykorzystanie try i except
try - próbuj robić, jeżeli napotkasz błąd, to except, dodanie pustej linii,
nowej linii, brak nazwiska przy danym imieniu.
Jeszcze można dodać finally - zawsze to rób pomimo wykonania try, except.
Można dodawać więcej except jeden po drugim z kolejnymi Error'ami.
Wykonały by się tylko te, które powstały w bloku try
'''

namesAndSurnames = []
with open("imionanazwiska.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        print(tuple(line.replace("\n", "").split(" ")))
        namesAndSurnames.append(tuple(line.replace("\n", "").split(" ")))

        
with open("imiona.txt", "w", encoding = "UTF-8") as file:      
    for item in namesAndSurnames:
       file.write(item[0] + "\n") 


with open("nazwiska.txt", "w", encoding = "UTF-8") as file:      
    for item in namesAndSurnames:
        if(len(item) == 2):
            file.write(item[1] + "\n")
        else:
            file.write("\n")


with open("nazwiska2.txt", "w", encoding = "UTF-8") as file:      
    for item in namesAndSurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
