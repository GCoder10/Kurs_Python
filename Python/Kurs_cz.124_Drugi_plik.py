from Kurs_cz_124__len__ import Rocket, RocketBoard
'''
    Import dwóch klas z innego pliku.
    Zdefiniowanie klas w innym pliku, zaimportowanie ich i dopiero
    kodowanie z otwartym drugim plikiem z klasami.

'''

# Plansza z ruchem rakiet przy inicjalizacji (__init__)
# Plansza z n rakietami na start ze zmianą wysokości
# Klasa RocketBoard ma ustawioną domyślną ilość rakiet na 5, gdyby
# nie został przesłany parametr.
board = RocketBoard(15)


# board. <-- nie będzie do niczego dostępu, rakiety istniały
# lokalnie dopóki działał konstruktor, trochę logika jak z 
# generatorami, tam też dostęp do elementu jest tylko w momencie
# jego wygenerowania.
# trzeba w klasie RocketBoard dopisać przedrostek self przed rockets,
# wtedy dopiero będzie odwołanie do rakiet stworzonych w ramach obiektu 
# board, instancji klasy.

board.rockets[0].altitude = 40
print(board.rockets[0].altitude)

# Kolejna metoda dunder - double underscore __
# Metody wywołujące się w określonym momencie:
# __init__ podczas inicjalizacji klasy przy pomocy obiektu (jej instancji)
# __getitem__ podczas odwoływania się do obiektu przy pomocy nawiasów, klamer: object[index]
# __setitem__ podczas odwoływania się do object[index] z jednoczesnym przypisaniem nowej wartości.
# Jest konieczne zadeklarowanie tego w dunder method, żeby program 'wiedział', do czego przypisać tak
# napisaną wartość, bo przecież może być wiele atrybutów w danym obiekcie.
board[0].altitude = 79
print(board[0].altitude)

board[0] = 180
print(board[0].altitude)


# Np. Rakieta1 jest na wysokości 2, Rakieta2 na 5, czyli distance = 3
# Metoda w klasie Rocket, wysokość rakiety przesłanej jako parametr do metody
# minus wysokość rakiety, od której chcemy zobaczyć (board[0].), jak daleko jest ta druga
print(board[0].get_distance(board[1]))


"""
    Liczenie odległości pomiędzy rakietami, gdy nie znajdują się 
    w jednej prostej linii. Pitagoras, punkt pomocniczy C.
    Wzór na liczenie dystansu pomiędzy punktami na wykresie:
    d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
    altitude - wysokość - y
    self.x - x
    W metodzie get_distance_via_pattern w klasie Rocket
    y2 i x2 = wysokość oraz x obiektu przesłanego do tej metody jako parametr,
    y1 i x1 = wysokość oraz x obiektu, względem którego sprawdzamy odległość, board[0]
"""
'''
    Liczenie dystansu pomiędzy rakietami, ale za pomocą metody 
    należącej do całej planszy rakiet a nie tylko do rakiety.
    Odległość od rakiety board[0] do rakiety board[4].

    Metody, które nie wykorzystują self, czyli odwołania się do 
    wartości atrybutów danego obiektu (instancji klasy) należy
    oznaczać jako statyczne.
    W tym celu nad metodą, którą chcemy oznaczyć jako statyczna
    dodajemy dekorator @staticmethod.
    Minusy:
    - nie ma self'a
    - można się odwołać wyłącznie do tego, co zostało przesłane do metody w klasie
    Plusy:
    - można wywołać taką metodę nawet jeżeli nie ma instancji klasy, obiektu
    - można stworzyć np. dwa obiekty na podstawie jednej klasy a następnie użyć statycznej metody
    z drugiej klasy bez wywoływania tej drugiej klasy (bez obiektu dla niej)


    Też kwestie optymalizacyjne:
    Jeżeli np. stworzymy listę z 5000 rakietami, to Python będzie musiał
    stworzyć 5000 powiązanych metod z tymi obiektami, bardzo duże zużycie
    niepotrzebne pamięci.
    Statyczna metoda będzie tylko jedna i konkretna, istnieje zawsze, bo 
    nie ma self'a.

    Wtedy koniecznie:
    RocketBoard.get_distance_via_pattern(board[0],board[2])
    zamiast:
    board.get_distance_via_pattern(board[0],board[2])
    ponieważ druga instrukcja sugeruje, że w metodzie get_distance_via_pattern
    jest gdzieś operowanie na wartościach atrybutów odnośnie tego konkretnego obiektu
    przy pomocy self.
'''
board[0] = 90
print(board.get_distance_via_pattern(board[0],board[4]))


board[0].x = 17
print(board.get_distance_via_pattern(board[0],board[2]))
print("\n\n\n\n\n\n\n\n\n\n")


rocket = Rocket(altitude=4, speed=100, x=12)
print(rocket.altitude)
print(rocket.speed)
print(rocket.x)
print("\n\n\n\n\n\n\n\n\n\n")

print(RocketBoard.get_distance_via_pattern(board[0],board[2]))



print("\n\n\n\n\n\n\n\n\n\n")
rocket1 = Rocket(speed=100,altitude=250,x=0)
rocket2 = Rocket(altitude=100)
print(RocketBoard.get_distance_via_pattern(rocket1,rocket2))


"""
    Dodawanie takich dopisków, że dany parametr jest jakiego typu:
     albo że rocket to Rocket.

    Klasa RocketBoard, metoda:
        def get_distance_via_pattern(rocket1: Rocket, rocket2: Rocket):
    określenie, że parametr rocket1 i rocket2 są typu Rocket.
    Dzięki temu, nawet jeżeli parametry nie nazywają się jasno (co do 
    reprezentowanego przez siebie typu), to tak jest lepiej:
        def get_distance_via_pattern(obj1: Rocket, obj2: Rocket):

    Metoda ta zwraca pierwiastek, czyli typ float:
        def get_distance_via_pattern(rocket1: Rocket, rocket2: Rocket) -> float:
    

    Rozszerzenie Pyright:
    by ms-pyright
    Będzie podpowiadać, gdy nie będziemy wiedzieli, jaki typ
    danych należy przesłać np. do metody:
        RocketBoard.get_distance_via_pattern(4,4)


    Zmienna:
        x = RocketBoard.get_distance_via_pattern(rocket1,rocket2)
    Automatycznie staje się typu float, ponieważ zostało określone
    jasno, że metoda ta zwraca typ float poprzez -> float
    Dzięki temu, gdy spróbujemy przypisać wynik tej metody do 
    zmiennej typu, np. int, zostanie wyświetlony błąd:
        x:int = RocketBoard.get_distance_via_pattern(rocket1,rocket2)



    Typy danych dodawane tak przez programiste nazywają się adnotacjami,
    'add note', dopisek, ma służyć bardziej dla programisty.


    Można także określać typy w parametrach z ustawieniami domyślnymi:
    W klasie Rocket, metoda:
        def __init__(self, speed:float = 1, altitude:float = 0, x:float = 0):
"""
'''
    W Python'ie najpierw tworzone są metody a dopiero potem klasa z tymi
    metodami.
    Dołączane są metody do tej klasy.
    Jednak w metodzie niestatycznej z self'em w klasie Rocket:
          def get_distance(self, rocket: "Rocket"):
    trzeba określić typ jako string, 
    najpierw metody, potem klasy z tymi metodami a na koniec 
    idzie interpretacja stringów.
    Gdyby napisać typ danych jako Rocket, wyskoczy błąd ze strony
    Python, ponieważ będzie zdefiniowany typ Rocket podczas gdy jeszcze
    nie ma tej klasy.
'''
"""
    from __future__ import annotations
    Informujemy interpreter, że będziemy korzystali z nowinek z 
    przyszłych wersji Python odnośnie adnotacji.        
"""
print("\n\n\n\n\n\n\n\n\n\n")
x = RocketBoard.get_distance_via_pattern(rocket1,rocket2)
print("\n\n\n\n\n\n\n\n\n\n")


# Nie można nadpisać zmiennej x jako np. x:int
# x:int = 4
newVariable:int = 4

# newVariable = 4.8


"""
    dunder metoda:
        __len__
    wywoływana w metodzie w określonym czasie, przy określonym
    użyciu instancji klasy, obiektu.
    - Pobranie długości obiektu.

    Musimy określić, co określa długość klasy, obiektu.
    (ilość rakiet na planszy = jej długość)
    Długość listy rockets, self.rockets, bo jest to odniesienie
    do tej konkretnej listy dla tej konkretnej instancji klasy, obiektu.


    Można wywoływać metody z klasy w innej metodzie w tej klasie w odniesieniu
    do konkretnej instancji klasy, obiektu przy pomocy self:
        return self.get_amount_of_rockets()
"""
board2 = RocketBoard(7)
print("\n\n\n\n\n\n\n\n\n\n")
print("len(board2)")
# Potrzebna dunder metoda __len__ do obsługi następnej instrukcji:
print(len(board2))


print("board2.get_amount_of_rockets()")
print(board2.get_amount_of_rockets())