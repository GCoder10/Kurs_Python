# TYPY ZAGNIEŻDŻONE, wypisanie wartości
# Zmienne
imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

# Krotki
osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')

# Listy w liście
listaGosci = [
                ['Arkadiusz', 28, 'mężczyzna'],
                ['Wioletta', 22, 'kobieta'],
                ['Kuba', 32, 'mężczyzna']
             ]

# Krotki w liście
listaGosciKrotki = [
                        ('Arkadiusz', 28, 'mężczyzna'),
                        ('Wioletta', 22, 'kobieta'),
                        ('Kuba', 32, 'mężczyzna')
                   ]

# Krotki w krotce
KrotkaGosciKrotki = (
                        ('Arkadiusz', 28, 'mężczyzna'),
                        ('Wioletta', 22, 'kobieta'),
                        ('Kuba', 32, 'mężczyzna')
                    )

# Zbiór z krotkami (set)
ZbiorGosciKrotki = {
                        ('Arkadiusz', 28, 'mężczyzna'),
                        ('Wioletta', 22, 'kobieta'),
                        ('Kuba', 32, 'mężczyzna')
                   }

# Zbiór z krotkami2 (set)
ZbiorGosciKrotki2 = {
                        ('Arkadiusz', 28, 'mężczyzna'),
                        ('Wioletta', 22, 'kobieta'),
                        ('Kuba', 32, 'mężczyzna'),
                        ('Katarzyna', 35, 'kobieta'),
                        ('Monika', 26, 'kobieta')
                    }

print("Arkadiusz: ")
print(listaGosci[0][0])
print("Arkadiusz wszystkie dane: ")
print(listaGosci[0])
print("Wioletta wszystkie dane: ")
print(listaGosci[1])
print("Kuba wiek 32: ")
print(listaGosci[2][1])
print("")
print("")
print("")
print("")
print("")
print("")
print("")


print("Arkadiusz zmiana wieku 30: ")
print(listaGosci[0][1])
listaGosci[0][1] = 30
print(listaGosci[0][1])

# Krotki w liście
print("")
print("")
print("")
print("")
print("")
print("")
print("==========KROTKI===========")
print("Arkadiusz: ")
print(listaGosciKrotki[0][0])
print("Arkadiusz wszystkie dane: ")
print(listaGosciKrotki[0])
print("Wioletta wszystkie dane: ")
print(listaGosciKrotki[1])
print("Kuba wiek 32: ")
print(listaGosciKrotki[2][1])
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Arkadiusz zmiana wieku 28: ")
print(listaGosciKrotki[0][1])
# listaGosciKrotki[0][1] = 30 <-- Błąd. Krotka.
print("")
print("")
print("")
print("")
print("")
print("Dodanie nowej osoby do listy krotek")
print("listaGosciKrotki.append(('KtośNowy', 45, 'mężczyzna'))")
listaGosciKrotki.append(('KtośNowy', 45, 'mężczyzna'))
print(listaGosciKrotki)




# Zbiór z krotkami (set)
print("")
print("")
print("")
print("")
print("")
print("")
print("==========Zbiór z krotkami===========")
print(ZbiorGosciKrotki)
print("Dodanie nowej osoby do zbioru z krotkami")
print("ZbiorGosciKrotki.add(('KtośNowyDoZbioru', 44, 'kobieta'))")
ZbiorGosciKrotki.add(('KtośNowyDoZbioru', 44, 'kobieta'))
print(ZbiorGosciKrotki)



print("")
print("")
print("")
print("")
print("")
print("")
print("==========Operacje na zbiorach===========")
SumaZbiorowGosciKrotki = ZbiorGosciKrotki | ZbiorGosciKrotki2
print("ZbiorGosciKrotki")
print(ZbiorGosciKrotki)
print("ZbiorGosciKrotki2")
print(ZbiorGosciKrotki2)
print("SumaZbiorowGosciKrotki")
print(SumaZbiorowGosciKrotki)
print("Czy ktoś nie zapisał sie dwukrotnie (& część wspólna): ")
CzescWspolnaZbiorowGosciKrotki = ZbiorGosciKrotki & ZbiorGosciKrotki2
print(CzescWspolnaZbiorowGosciKrotki)


# Przetwarzanie danych z typów zagnieżdżonych
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
for imie, wiek, plec in ZbiorGosciKrotki:
    print("Imie:", imie)
    print("Wiek:", wiek)
    print("Płeć:", plec)
    print("\n") # Dodaje ENTER
