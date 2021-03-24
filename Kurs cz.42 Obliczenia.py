import Kurs_cz42_Aplikacja_wielomodułowaJak_zaimportować_własny_moduł

importedModule = Kurs_cz42_Aplikacja_wielomodułowaJak_zaimportować_własny_moduł;
print("importedModule.pole_kwadratu(4): ")
print(importedModule.pole_kwadratu(4))


wybor = input("""Wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez\n\n""")

if (wybor == '1'):
    a = float(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi:", importedModule.pole_kwadratu(a))
elif (wybor == '2'):
    a = float(input("Podaj 1-wszy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    print("Pole prostokąta wynosi:", importedModule.pole_prostokata(a, b))
elif (wybor == '3'):
    r = float(input("Podaj promień koła: "))
    print("Pole koła wynosi:", importedModule.pole_kola(r))
elif (wybor == '4'):
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", importedModule.pole_trojkata(a, h))
elif (wybor == '5'):
    a = float(input("Podaj 1-wszy bok trapezu: "))
    b = float(input("Podaj 2-gi bok trapezu: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi:", importedModule.pole_trapezu(a, b, h))
