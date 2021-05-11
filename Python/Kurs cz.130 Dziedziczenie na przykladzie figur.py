"""
    Stworzenie trzech klas:
    1) Rectangle - prostokąt.
    2) Square - kwadrat.
    3) Cube - sześcian.

    a) Stworzenie konstruktorów (__init__) - dunder metody - double underscore - metody
    wywołujące się przy określonym użyciu klasy, jej instancji - obiektu.
    b) Metody obliczające powierzchnię kwadratu, prostokąta,
    sześcianu.
    c) Metoda obliczająca objętość sześcianu.

    Wykorzystanie dziedziczenia, aby nie powtarzać kodu.
"""
'''
    Wykorzystanie self -> działanie na atrybutach przynależących tylko do
    danej instancji klasy, obiektu stworzonego na podstawie tej klasy (dostęp 
    za pomocą takiego obiektu do metod klasy itd.).
    Do konstruktora init zostają przysłane parametry, które stają się wartościami
    dla atrybutów należących do takiej instancji klasy.
'''
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # pass # pass'ujemy, znak dla kompilatora, że tutaj nic się nie dzieje ciekawego.
    def count_surface_area(self): # powierzchnia, surface
        return self.width * self.height # Funkcja, w C++/C++11 też, z return to funkcja, bez return to procedura (void)


class Square(Rectangle): # Dziedziczenie z klasy wyżej - klasy rodzica
    def __init__(self, sideLength):
        # self.sideLength = sideLength -> metoda super()
        super().__init__(sideLength,sideLength) # Skorzystanie z konstruktora z klasy wyżej.
        print("Dostęp do atrybutów z klasy wyżej: ")
        print("width:",self.width)
        print("height:",self.height)
    # pass

class Cube(Square): # Czyli zyskujemy dostęp do metod z dwóch klas: Rectangle oraz Square
    def count_surface_area(self): # Nadpisanie metody z klasy wyżej.
        return super().count_surface_area() * 6 # Wykorzystanie konstruktora z klasy wyżej przy pomocy metody super(), 
        # przemnożenie wyniku zwróconego przez metodę z klasy wyżej przez 6 i 
        # zwrócenie tego (zwracanie podwójne można powiedzieć).
    # Cube() -> VSC wyskoczy podpowiedź o możliwości użycia parametru: sideLength
    # pass
    def count_volume(self): # Funkcji nie ma w klasie rodzic.
        return super().count_surface_area() * self.height


cube = Cube(2) # cube = instancja klasy Cube(), obiekt

print("Dostęp do atrybutów z klasy położonej najwyżej w kontekście dziedziczenia tutaj:")
print("cube.width:",cube.width)
print("cube.height:",cube.height)

print("\n\n\n\n\n\n\n\n\n\n")

print("Powierzchnia kwadratu (4): ")
square = Square(2)
print(square.count_surface_area())

print("\n\n\n\n\n\n\n\n\n\n")
print("Powierzchnia kwadratu (9): ")
square = Square(3)
print(square.count_surface_area())




print("\n\n\n\n\n\n\n\n\n\n")
print("Powierzchnia sześcianu (): ")
print("Wykorzystanie pola powierzchni kwadratu: ")
cube = Cube(3)
print("Powierzchnia sześcianu (54): ")
print(cube.count_surface_area())


print("\n\n\n\n\n\n\n\n\n\n")
print("objętość sześcianu (27): ")
print(cube.count_volume())