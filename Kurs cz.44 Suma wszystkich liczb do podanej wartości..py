"""
    Program liczący sumę wszystkich liczb od 1 do podanej liczby

    Np. dla 5
    1+2+3+4+5
    zwróci
    15


    Najprostszy sposób - pętla:
    range(6)
    1,2,3,4,5
"""
# Pierwszy sposób na rozwiązanie tego zadania:
def sumuj_do(liczba):
    suma = 0
    #print("Wypisanie liczb: ")
    #for liczba in range(1, liczba):
    #    print(liczba)
    for liczba in range(1, liczba + 1):
        suma += liczba
    return suma


print("\n\n\n\n[Pierwszy sposób] Suma 5: ")
print(sumuj_do(5))
print("\n\n\n\n[Pierwszy sposób] Suma 25: ")
print(sumuj_do(25))

# Drugi sposób na rozwiązanie tego zadania:
'''
    Do funkcji sum przesłanie listy wyrażeniowej.
'''
def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

print("\n\n\n\n[Drugi sposób] Suma 5: ")
print(sumuj_do2(5))
print("\n\n\n\n[Drugi sposób] Suma 25: ")
print(sumuj_do2(25))



# Trzeci sposób na rozwiązanie tego zadania:
'''
    Odpowiedni algorytm - zależność w nim istniejąca

    Dla sumy 5
    1,2,3,4,5
    (1 + 5) / 2 * 5 = 15
    Wzór na ciąg arytmetyczny
'''
def sumuj_do3(liczba):
    return (1 + liczba) / 2 * liczba


print("\n\n\n\n[Trzeci sposób] Suma 5: ")
print(sumuj_do3(5))
print("\n\n\n\n[Trzeci sposób] Suma 25: ")
print(sumuj_do3(25))


# Czwarty i piąty sposób:
'''
    Wyrażenie zbioru {} i wyrażenie generatora ()
'''
def sumuj_do4(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})

def sumuj_do5(liczba):
    return sum((liczba for liczba in range(1, liczba + 1)))

print("\n\n\n\n[Czwarty sposób] Suma 5: ")
print(sumuj_do4(5))
print("\n\n\n\n[Piąty sposób] Suma 25: ")
print(sumuj_do5(25))
