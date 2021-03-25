import Kurs_cz42_Aplikacja_wielomodułowaJak_zaimportować_własny_moduł
from enum import Enum
from enum import IntEnum

importedModule = Kurs_cz42_Aplikacja_wielomodułowaJak_zaimportować_własny_moduł;
print("importedModule.pole_kwadratu(4): ")
print(importedModule.pole_kwadratu(4))

"""
    enumeration - spis - wyliczenie - enum
"""
print("Nowy typ: ")
print(Enum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez'))



print("Nowy typ jako lista: ")
print(list(Enum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')))

# Przyjmuje się, że zmienne przechowujące wartości związane z Enum piszemy
# z dużych liter.
Menu_Figury = Enum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')
IntMenu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')
IntMenu_Figury2 = IntEnum('Menu_Figury', 'Kwadrat, Prostokąt, Koło, Trójkąt, Trapez')
IntMenu_FiguryLista = IntEnum('Menu_Figury', ['Kwadrat', 'Prostokąt', 'Koło', 'Trójkąt', 'Trapez'])
IntMenu_FigurySłownik = IntEnum('Menu_Figury', {'Kwadrat': 4, 'Prostokąt': 52, 'Koło': 24, 'Trójkąt': 3, 'Trapez': 35})


print("IntEnum z przecinkami: ")
print(list(IntMenu_Figury2))

print("IntEnum z listą: ")
print(list(IntMenu_FiguryLista))


print("IntEnum ze słownikiem: ")
print(list(IntMenu_FigurySłownik))

wybor = int(input("""Wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez\n"""))

if (wybor == Menu_Figury.Kwadrat.value):
    a = float(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi:", importedModule.pole_kwadratu(a))
elif (wybor == IntMenu_Figury.Prostokąt):
    a = float(input("Podaj 1-wszy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    print("Pole prostokąta wynosi:", importedModule.pole_prostokata(a, b))
elif (wybor == IntMenu_Figury.Koło):
    r = float(input("Podaj promień koła: "))
    print("Pole koła wynosi:", importedModule.pole_kola(r))
elif (wybor == Menu_Figury.Trójkąt.value):
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", importedModule.pole_trojkata(a, h))
elif (wybor == IntMenu_Figury.Trapez):
    a = float(input("Podaj 1-wszy bok trapezu: "))
    b = float(input("Podaj 2-gi bok trapezu: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi:", importedModule.pole_trapezu(a, b, h))
