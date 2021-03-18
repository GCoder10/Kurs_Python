# dictionary - słownik
"""
[] - listy
()
   - krotki
{} - słownik
Kolejny sposób na przechowywanie danych.
Słownik przechowuje elementy oraz ich wartości, a dokładniej:
KLUCZ - wartość
Logika jak w słowniku: słowo oraz jego definicja, co się pod tym słowem kryje.

Kolejność elementów w słowniku nie ma znaczenia.
"""

slownik = {49: 'Arkadiusz', 70: 'Wioletta', 71: 'Anna', 49: 'Nadpisanie 49'}


print(slownik)
print("")
print("")
print("")
print("")
print("")
print("")



print("Przed podmianą klucza numer 49: ")
print(slownik)
slownik[49] = 'Jakub'
print("Po podmianie klucza numer 49: ")
print(slownik)


print("")
print("")
print("")
print("")
print("")
print("")
print("Przed dodaniem nowej osoby numer 50: ")
print(slownik)
slownik[50] = 'Nowa_Osoba'
print("Po dodaniu nowej osoby numer 50: ")
print(slownik)

print("")
print("")
print("")
print("")
print("")
print("")
# Wartość string też może być kluczem
slownik2 = {'imie': 'Arkadiusz', 'nazwisko': 'Nowak'}
print(slownik2)
print(slownik2['imie'])
print(slownik)
print(slownik[71])


"""
    .get()
"""
print("")
print("")
print("")
print("")
print("")
print("Funkcja get do uzyskania wartości ze słownika .get(70)")
print(slownik)
print(slownik.get(70))



"""
    .update({KLUCZ: wartość}) - dodanie nowego elementu na końcu słownika
    Można dodawać wiele nowych elementów na raz, czyli w sumie można np.
    uzupełnić słownik o nowy słownik.
"""
print("")
print("")
print("")
print("")
print("")
print("Przed dodatniem nowego elementu .update({}): ")
print(slownik)
slownik.update({405: 'Nowa_Osoba Kowalski'})
print("Po dodatniu nowego elementu .update({}): ")
print(slownik)




"""
    del(slownik[KLUCZ]) - usunięcie danego klucza oraz przypisanej do niego
    wartości.
"""
print("")
print("")
print("")
print("")
print("")
print("Przed usunięciem klucza del(slownik[70]): ")
print(slownik)
del(slownik[70])
print("Po usunięciu klucza del(slownik[70]): ")
print(slownik)




"""
    pop(KLUCZ) - usunięcie elementu ze słownika (KLUCZ) oraz przypisanej do
    niego zawartości.
    pop zwraca wartość przed jej usunięciem, więc można wykorzystać ją
    gdzieś dalej.
"""
print("")
print("")
print("")
print("")
print("")
print("Przed usunięciem klucza pop(405): ")
print(slownik)
slownik.pop(405)
print("Po usunięciu klucza pop(405): ")
print(slownik)






"""
    .popitem() - usuwa ostatni element słownika, też go zwraca przed usunięciem.
"""
print("")
print("")
print("")
print("")
print("")
print("Przed usunięciem klucza popitem(): ")
print(slownik)
slownik.popitem()
print("Po usunięciu klucza popitem(): ")
print(slownik)






"""
    len() - funkcja zwraca ilość KLUCZY w słowniku
"""
print("")
print("")
print("")
print("")
print("")
print("Ilość kluczy len(slownik): ")
print(slownik)
print(len(slownik))






"""
    clear() - wyczyszczenie zawartości słownika
"""
print("")
print("")
print("")
print("")
print("")
print("Przed clear(): ")
print(slownik)
slownik.clear()
print("Po clear(): ")
print(slownik)
