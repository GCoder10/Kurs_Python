'''
    Każdy nowy plik w Python .py to jest moduł.
    Moduły dzielimy na trzy typy:
    1. Do zaimportowania w każdej chwili, np. math. Python Standard Library
    2. Takie, które trzeba zainstalować z zewnętrznych źródeł.
    3. Takie, które piszemy sami.

    Pliki nasze do zaimportowania i moduł, w którym będziemy importować
    muszą być w tym samym folderze.
'''
import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

"""
    Środowiska programistyczne lepsze do aplikacji wielomodułowych:

        PyCharm
        Visual Studio Code
        Atom
        Spyder
"""
