import time

def function_performance(func, *arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):  
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

"""
    Przesyłanie do funkcji function_performance dwóch argumentów jako jeden.
    Czyli wykorzystanie do tego tzw. argumentu wielowartościowego.
    *arg = możemy przesłać więcej niż jeden argument,
    nawiązanie do tablic z C/C++?, arg jako nazwa tablicy (wskaźnik na jej
    pierwszy element [jego adres]) przechowującej argumenty tej funkcji jako
    swoje wartości do przekazywania jako parametr tej funkcji?
    Jeżeli byłoby to oparte o dynamiczne alokowanie pamięci, np. new double,
    to czy zwróci NUL przy braku możliwości zarezerwowania pamięci obok siebie
    dla danych, a może to vector z C++11?

    Krotka, generatory są szybsze.
    Argumenty są przechowywane wtedy w krotce.
    Zbiór w krotce.
    Krotka jest najlepszym wyborem zaraz po generatorze jeżeli chodzi
    o przetwarzanie dużych ilości danych ze względu na bardzo małą zajmowaną
    ilość miejsca w pamięci. Generator zajmuje najmniej, ale nie mamy dostępu
    do danych wygenerowanych przez generator już po np. wyświetleniu ich /
    przekazaniu gdzieś indziej.
""" 

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False


'''
    Interpreter "wie", jakie to są argumenty do *arg po kolejności
    przekazywanych argumentów, dopóki argumenty są nienazwane, how_many_times
    już jest nazwany.
'''
print("Czas wykonania dla szukania elementu w zbiorze")
print(function_performance(is_element_in,
                           450,
                           setContainer,
                           how_many_times = 500000))


print("Czas wykonania dla szukania elementu w liscie")
print(function_performance(is_element_in,
                           450,
                           listContainer,
                           how_many_times = 500000))

"""
    Argumenty pozycyjne (nienazwane) przed argumentami nazwanymi.
    Jeżeli nie chcemy pamiętać o tej kolejności podczas przekazywania wielu
    argumentów do funkcji, to trzeba trochę przebudować funkcję.
"""
def function_performance2(func, how_many_times = 1, *arg):
    sum = 0
    print("arg[0], function_performance2: ")
    print(arg[0])
    for i in range(0, how_many_times):  
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum


print("Czas wykonania dla szukania elementu w zbiorze")
print(function_performance2(is_element_in,
                           500000,
                           450,
                           setContainer))


print("Czas wykonania dla szukania elementu w liscie")
print(function_performance2(is_element_in,
                           500000,
                           450,
                           listContainer))



"""
    **arg - jeżeli chcemy przekazywać wiele argumentów nazwanych
    Słownik
"""
def function_performance3(func, how_many_times = 1, **arg):
    sum = 0

    
    print("arg.get('what_value'), function_performance3: ")
    print(arg.get("what_value"))

    
    print("arg.get('container'), function_performance3: ")
    print(arg.get("container"))


    # Sprawdzanie w samej funkcji, czy w argumentach znajduje się coś, co jest
    # równe tyle i tyle, wtedy robienie czegoś innego itp.


    for i in range(0, how_many_times):  
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum


print("Czas wykonania dla szukania elementu w zbiorze")
print(function_performance3(is_element_in,
                           500000,
                           what_value = 450,
                           container = setContainer))


print("Czas wykonania dla szukania elementu w liscie")
print(function_performance3(is_element_in,
                           500000,
                           what_value = 450,
                           container = listContainer))
