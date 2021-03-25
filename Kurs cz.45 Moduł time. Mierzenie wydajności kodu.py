import time

"""
    Mierzenie wydajności skryptu:


    Czas wykonania jest różny w zależności od zajętości procesora,
    spraw optymalizacyjnych twórców Python.
    Zależy też to od wielkości przerabianych danych:
    Coś, co jest szybsze (algorytm - sposób) dla mniejszej ilości danych, nie
    musi być szybsze dla większej ilości danych do przetworzenia.
"""
def finish_timer(start):
    end = time.perf_counter()
    return end - start


# Pierwszy sposób na rozwiązanie tego zadania:
def sumuj_do(liczba):
    suma = 0
    # Dodanie listy w ramach sztucznego przedłużenia czasu wykonania:
    x = []
    for liczba in range(1, liczba + 1):
        suma += liczba
        x.append(liczba)
    return suma

start = time.perf_counter()
print("\n\n\n\n[Pierwszy sposób] Suma 5: ")
print(sumuj_do(50000))
print("\n\n\n\n[Pierwszy sposób] Suma 25: ")
print(sumuj_do(25000))
print("Czas wykonania (sekundy): ")
print(finish_timer(start))

# Drugi sposób na rozwiązanie tego zadania:
'''
    Do funkcji sum przesłanie listy wyrażeniowej.
'''
def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

start = time.perf_counter()
print("\n\n\n\n[Drugi sposób] Suma 5: ")
print(sumuj_do2(50000))
print("\n\n\n\n[Drugi sposób] Suma 25: ")
print(sumuj_do2(25000))
print("Czas wykonania (sekundy): ")
print(finish_timer(start))




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


start = time.perf_counter()
print("\n\n\n\n[Trzeci sposób] Suma 5: ")
print(sumuj_do3(50000))
print("\n\n\n\n[Trzeci sposób] Suma 25: ")
print(sumuj_do3(25000))
print("Czas wykonania (sekundy): ")
print(finish_timer(start))



# Czwarty i piąty sposób:
'''
    Wyrażenie zbioru {} i wyrażenie generatora ()
'''
def sumuj_do4(liczba):
    return sum({liczba for liczba in range(1, liczba + 1)})

def sumuj_do5(liczba):
    return sum((liczba for liczba in range(1, liczba + 1)))

start = time.perf_counter()
print("\n\n\n\n[Czwarty sposób] Suma 5: ")
print(sumuj_do4(50000))
print("\n\n\n\n[Piąty sposób] Suma 25: ")
print(sumuj_do5(25000))
print("Czas wykonania (sekundy): ")
print(finish_timer(start))

