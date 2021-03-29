import time

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):  
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

"""
    Funkcja ma sprawdzać, czy dany element istnieje w zbiorze (set {}) czy też liście
    (list []) i sprawdzenie, czego sprawdzenie jest szybsze.
""" 
def is_element_in(what_value):
    if what_value in setContainer:
        return True
    else:
        return False

def is_element_in2(what_value):
    if what_value in listContainer:
        return True
    else:
        return False


print("Czas wykonania dla szukania elementu w zbiorze")
print(function_performance(is_element_in, 450, how_many_times = 500000))


print("Czas wykonania dla szukania elementu w liscie")
print(function_performance(is_element_in2, 450, how_many_times = 500000))
# Zbiór jest o wiele razy szybszy niż lista ze względu na swoją specyfikę.
# W zbiorze nie trzeba pilnować kolejności elementów, w liście już tak.
# Dodatkowo zbiór daje nam szereg rozwiązań np. do porównywania danych między serwerami,
# chodzi o porównywanie zbiorów, lub sprawdzanie, czy dany zbiór jest podzbiorem innego zbioru,
# suma zbiorów, odejmowanie, części wspólne itp.
