"""
    Obiekt to zmienna, która ma więcej możliwości.
    Można wywołać na nim "funkcje".
    Może mieć więcej niż 1 wartość.

    Obiekty immutable: bool, int, float, tuple, str

    immutable - niezmienne
    mutable - zmienny
"""
a = 4 # Obiekt = zmienna, ma więcej możliwości niż przechowywanie wartości.
print("Długość bitowa a, a.bit_length(), 3: ")
print(a.bit_length()) # Obiekt posiada metody, których można na nim użyć (na przechowywanej wartości).


# Lista, też obiekt, reszta też, np. słownik, krotka, generator, zbiór.

listSample = [1, 4, 512, 24]

listSample2 = listSample # Przypisanie adresu obiektu do obiektu a nie wartości

listSample2.append(465)
print("listSample: ")
print(listSample)


print("listSample2.append(465): ")
print("listSample2: ")
print(listSample2)
print("\n\n\n\n\n\n\n\n\n\n\n")

# Funkcja id zwraca adres przechowywania danego obiektu
# Przy okazji wygląda na to, że adresy są automatycznie zamieniane
# z systemu szesnastkowego (HEX) na dziesiętny
# W C/C++/C++11 adresy są w HEX
print("Adres listSample, id(listSample): ")
print(id(listSample))

print("Adres listSample2, id(listSample2): ")
print(id(listSample2))


"""
    ==============================================================
    Listy itd = obiekty mutable, zmienne
    Zmienne int, float itp. = obiekty immutable, niezmienne
    = Zmiana miejsca wskazywania na nowy adres, na inny obiekt
"""
b = a
b = 7
print("a = 4: ")
print(a)
print("b = 7: ")
print(b)
print("\n\n\n\n\n\n\n\n\n\n\n")

print("Adres a, id(a): ")
print(id(a))
print("Adres a, id(b): ")
print(id(b))
print("\n\n\n\n\n\n\n\n\n\n\n")

"""
    ===============================================================
    Append jak i [0] = 7 zadziała tak samo, zmieni się w obu obiektach
    wartość.
    Ponieważ lista, krotka, zbiór, słownik, generator są to obiekty
    zmienne, mutable.
    W przypadku int, float itd. tak to nie działa, ponieważ są to
    obiekty immutable, niezmienne.
"""
listSample = [1, 4, 512, 24]
listSample2 = listSample
listSample2[0] = 7

print("listSample: ")
print(listSample)


print("listSample2[0] = 7: ")
print("listSample2: ")
print(listSample2)
print("Adres listSample, id(listSample): ")
print(id(listSample))

print("Adres listSample2, id(listSample2): ")
print(id(listSample2))
print("\n\n\n\n\n\n\n\n\n\n\n")

"""
    ===============================================================
    4 i 4 to jest ten sam obiekt i zachodzi optymalizacja, dlatego
    wychodzi na to, że dwa obiekty niezmienne wskazują na ten sam
    adres.
"""
k = 4
h = 4
print("Adres k, id(k): ")
print(id(k))
print("Adres h, id(h): ")
print(id(h))

h = 20
print("Adres k, id(k): ")
print(id(k))
print("Adres h, id(h): ")
print(id(h))

print("\n\n\n\n\n\n\n\n\n\n\n")

"""
    ===============================================================
"""
c = 5
print("Zmienna globalna c = 5, adres: ")
print(id(c))
def add(c, amount = 1):
    print("Skorzystanie ze zmiennej globalnej, adres: ")
    print(id(c))
    c = c + amount
    print("Zmienna lokalna c w funkcji, adres: ")
    print(id(c))
add(c)
print("Wartość c, c = 5: ")
print(c)
    
print("\n\n\n\n\n\n\n\n\n\n\n")

"""
    ===============================================================
    Obiekt mutable, zmienny, zachodzi zmiana na oryginale (lista)
    Obiekt immutable, niezmienny, nie zachodzi zmiana na oryginale (int)
"""
def append_element_to_list(listka, element):
    print("Adres listy, argument przychodzący do funkcji, przed dodaniem elementu: ")
    print(id(listka))
    listka.append(element)
    print("Adres listy, argument przychodzący do funkcji, po dodaniu elementu: ")
    print(id(listka))
print("Adres listy, przed przesłaniem do funkcji: ")
print(id(listSample)) 
append_element_to_list(listSample, 5)
print(listSample)
print("\n\n\n\n\n\n\n\n\n\n\n")

"""
    ===============================================================
"""
def append_element_to_list(listka, element):
    print("Adres listy, argument przychodzący do funkcji, przed listka = [2, 4, 20]: ")
    print("Adres oryginalny: ")
    print(id(listka))
    listka = [2, 4, 20] # Przypisanie innego obiektu do listka, innego adresu
    print("Adres listy, argument przychodzący do funkcji, po listka = [2, 4, 20]: ")
    print("Adres inny: ")
    print(id(listka))
print("Adres listy, przed przesłaniem do funkcji: ")
print("Adres oryginalny: ")
print(id(listSample)) 
append_element_to_list(listSample, 58)
print(listSample)
print("\n\n\n\n\n\n\n\n\n\n\n")
