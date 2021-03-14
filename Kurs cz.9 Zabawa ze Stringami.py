imie = "PrzykładoweImie"
print(imie)

nazwisko = "PrzykładoweNazwisko"
print(nazwisko)


print(imie + nazwisko)

print(imie + " " + nazwisko)

pelneImieNazwisko = imie + " " + nazwisko
print(pelneImieNazwisko)



dlugiString = "Jakiś długi Tekst 1\
               Jakiś długi Tekst 2\
               Jakiś długi Tekst 3\
               Jakiś długi Tekst 4"
print(dlugiString)

dlugiStringZUzyciemKomentarza = """Jakiś długi tekst 11
 Jakiś długi tekst 12
 Jakiś długi tekst 13
 Jakiś długi tekst 14"""

print(dlugiStringZUzyciemKomentarza)

#Wybieranie czegoś ze stringa:
#String jako tablica char:
print(nazwisko[0]) #P
print(nazwisko[4]) #k

'''
    W Python można pobrać od razu ostatni element przy pomocy
    indeksu -1.
    Można po prostu poruszać się po takiej tablicy przy
    pomocy ujemnych indeksów (od ostatniego elementu).
'''
print(nazwisko[-1]) #o
print(nazwisko[-3]) #s

'''
    : - zakres wybranych elementów.
'''
print(nazwisko[:]) #całe nazwisko
print(nazwisko[0:7]) #Przykła
print(nazwisko[0:-7]) #PrzykładoweN
print(nazwisko[:-1]) #Całe nazwisko bez ostatniego znaku
