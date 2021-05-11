"""
    przyporządkowanie - przynależy, należy do, jest jedną ze składowych, 
    jest częścią czegoś.

    Agregacja - łączyć w całość, zawieranie się, gromadzenie - tworzenie 
    obiektu składowego.

    cuboid
"""
'''
    
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


class Cube(Square):
    def count_surface_area(self): 
        return super().count_surface_area() * 6 
    def count_volume(self): 
        return super().count_surface_area() * self.height


cube = Cube(2) 

print(cube.count_surface_area())