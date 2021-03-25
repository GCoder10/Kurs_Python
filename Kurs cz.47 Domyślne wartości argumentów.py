"""
    Domyślne argumenty:

        Jeżeli funkcja oczekuje na wiele argumentów a dostanie tylko
        część z nich, to reszta przyjmie wartości domyślne.
"""

def increment(x, amount = 1):
    return x + amount

a = increment(4, 20)
print(a)


a = increment(4)
print(a)

#===============================================================================
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

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):  
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum

def show_message(message):
    print(message)

function_performance(show_message, "Wiadomość przesłana")


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
print("function_performance: ")
print(function_performance(sumuj_do, 50000))

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



# Czas wykonania, przekazywanie funkcji do funkcji. Funkcja jako argument.
print("\n\n\n\n\n\n\n\n\n\n\nfunction_performance: ")
print("sumuj_do: ")
print(function_performance(sumuj_do, 50000))
print("sumuj_do2: ")
print(function_performance(sumuj_do2, 50000))
print("sumuj_do3: ")
print(function_performance(sumuj_do3, 50000))
print("sumuj_do4_x4: ")
print(function_performance(sumuj_do4, 50000, 4))
print("sumuj_do5_x100: ")
print(function_performance(sumuj_do5, 50000, 100))
