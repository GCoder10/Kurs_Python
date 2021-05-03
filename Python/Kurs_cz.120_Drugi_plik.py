from Kurs_cz_120_Odleglosc_od_jednej_do_drugiej_rakiety import Rocket, RocketBoard
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

board[0] = 90
print(board[0].get_distance_via_pattern(board[6]))


board[0].x = 17
print(board[0].get_distance_via_pattern(board[6]))
print("\n\n\n\n\n\n\n\n\n\n")


rocket = Rocket(altitude=4, speed=100, x=12)
print(rocket.altitude)
print(rocket.speed)
print(rocket.x)