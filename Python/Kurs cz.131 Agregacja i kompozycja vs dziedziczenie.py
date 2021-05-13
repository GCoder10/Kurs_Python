"""
    przyporządkowanie - przynależy, należy do, jest jedną ze składowych, 
    jest częścią czegoś.

    Agregacja - łączyć w całość, zawieranie się, gromadzenie - tworzenie 
    obiektu składowego.

    kompozycja

    cuboid
"""
'''
    Kiedy powinno się używać zwykłego dziedziczenia a kiedy przyporządkowania
    /agregacji?:
     -  Gdy druga klasa jest ewidentnie podklasą klasy rodzic, jak tutaj,
        kwadrat jest podtypem prostokąta, jest wystarczająco duże powiązanie obu
        klas aby był sens zastosowania normalnego dziedziczenia.
        Gdy coś drugiego jest podtypem tego pierwszego.
     -  Kwadrat, sześcian, nie mają dużo wspólnego, więc tutaj normalne 
        dziedziczenie najmniej pasuje, druga rzecz nie jest podtypem tej
        pierwszej.
        Sześcian nie jest podtypem kwadratu.
        Korzystamy wtedy z przyporządkowania.
     -  Agregacja - podtyp przyporządkowania.
        Zawieramy kwadrat w sześcianie, tworzymy obiekt składowy.
     -  Kompozycja - polega na tym samym co agregacja czy też przyporządkowanie,
        tyle że, obiekt, który przyporządkowujemy nie może istnieć bez klasy, do 
        której właśnie ten obiekt przyporządkowujemy.
        Silna zależność między obiektami, drugi nie może istnieć bez istnienia
        tego pierwszego.
'''
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle): 
    def __init__(self, sideLength):
        super().__init__(sideLength,sideLength) 
        print("Dostęp do atrybutów z klasy wyżej: ")
        print("width:",self.width)
        print("height:",self.height)


class Cube(): # Nie powinno być tutaj dziedziczenia z dwóch klas na raz
# Nie używać dziedziczenia gdzie popadnie
    def __init__(self, square: Square): # Inicjalizator klasy oczekuje na parametr tybu Square
        self.square = square # Agregacja - Kwadrat może istnieć bez sześcianu.
        self.height = square.height # height odziedziczony po klasie Rectangle w klasie Square
    def count_surface_area(self): 
        return self.square.count_surface_area() * self.height # W klasie Square dostęp do metody count_surface_area() odziedziczonej po klasie Rectangle 
    def count_volume(self): 
        return self.square.count_surface_area() * self.height
"""
    Lepszym rozwiązaniem było by tutaj przyporządkowanie obiektu, instancji klasy
    do innej klasy - przyporządkowanie - jest częścią czegoś obiekt nowy.
"""
'''
    Przyporządkowanie do atrybutu figury, która została przysłana,
    może tutaj to być Rectangle ale również Square.
    Przesyłamy figurę do danego obiektu, instancji klasy, przyporządkowujemy 
    ją do atrybutu tego obiektu i dzięki temu uzyskujemy dostęp do metod
    należących do klasy do której przynależy nadesłana figura.
'''

class Cuboid(): # Prostopadłościan
    def __init__(self, figure, height): # Inicjalizator, konstruktor
        self.figure = figure
        self.height = height
    def count_volume(self): # Objętość
        return self.figure.count_surface_area() * self.height

"""
    2,3 -> do metody count_surface_area(self) z klasy Rectangle = 6
    Cuboid(6, 4) -> do metody count_volume z klasy Cuboid = 24
"""
cuboid = Cuboid(Rectangle(2,3), 4) # Bardziej czytelne niż np. Cuboid(2, 3, 4)

print(cuboid.count_volume())