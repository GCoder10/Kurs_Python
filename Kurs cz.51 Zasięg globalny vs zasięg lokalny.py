def add():
    c = 5
    return c

add()
# print(c) - zmienna lokalna dla funkcji add
# return c, zamienia add() na zawartość, nie zostało nigdzie zapisane.
'''
    W C++ zmienne globalne mają automatycznie przypisywane 0 wartości,
    zmienne lokalne w przypadku braku przypisania wartości mogą przyjmować
    losowe dane z pamięci, np. z innego programu.
'''
c = 1 # Zmienna globalna
c = add()
print("c = add() [5] ")
print(c)



"""
    Zmienna lokalna przyjmie napotkaną wartość zmiennej globalnej
"""
def add2():
    print(d)


d = 100
print("d = 100 [100]")
add2()


"""
    Wpływanie zmiennej lokalnej na globalną.
    global a, skorzystanie ze zmiennej globalnej w zmiennej lokalnej.
    W funkcji można tak operować na wartości zmiennej globalnej.
"""
def add3():
    global a
    a = a + 4
    print(a)


a = 1
print("a = 1 [5]")
add3()
print(a)



"""

"""
def add4(b):
    b = 40
    print(b)


b = 20
print("b = 20 [40], [20]")
add4(b) # Zmienna lokalna nadpisze wartość na 40, ale tylko lokalnie
print(b) # Zmienna globalna nadal = 20
