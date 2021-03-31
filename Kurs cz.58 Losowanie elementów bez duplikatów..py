# ============================================================================
"""
    sample przyjmuje jako pierwszy parametr listę, z jakiej będzie unikalnie
    losować, może być range, tutaj będzie to od 0 do (total_amount + 1), drugi
    parametr to, ile takich unikalnych liczb ze wcześniej przekazanej listy
    ma wylosować.

    Funkcja zwraca listę

     + 1, żeby także losowało z przekazywaną liczbą włącznie.

    ========================================================================
    Lotto
    Wybieranie 6 unikalnych liczb z 49

    sample - próbka / przykład
    Funkcja losuje unikalnie
""" 
import random

def choose_random_numbers(amount, total_amount):
    print("random.sample(range(total_amount + 1), amount): ")
    print(random.sample(range(total_amount + 1), amount))
    random.sample(range(total_amount + 1), amount)


choose_random_numbers(6, 49)
# ============================================================================
'''
    Shuffle - randomizes entire list
    Przetasować
    Zmienia kolejność jakiegoś zbioru elementów.
    Funkcja działająca na oryginale.
    Obiekty - listy, zbiory, itd. są mutable - zmienne, więc dlatego
    funkcja działa na oryginale.
    Niezmienne - immutable - są obiekty takie jak: int, double, float itp.


    Użycie sample z set (zbiór) aby faktycznie nie było duplikatów,
    brak duplikatów - właściwość zbiorów w Python.
    Szybciej działają od list (wszystko jest wrzucane do "jednego worka", podczas
    gdy w liście musi być zachowana kolejność, listy najwięcej zajmują miejsca
    w pamięci jeżeli chodzi o operowanie na bardzo dużych danych).

    Listy - zachowanie kolejności. Dużo możliwości operowania na danych, dlatego
    zajmują aż można powiedzieć najwięcej miejsca w pamięci. []

    
    Zbiór - operacje na zbiorach, suma, elementy wspólne, suma zbiorów, zbiór A
    minus zbiór B, czy zbiór A jest podzbiorem B. Idealne do testowania /
    porównywania danych między np. serwerami.
    Właściwość zbioru: elementy powtarzające się zostaną przerobione na unikalne.
    {}

    
    Słownik - KLUCZ: wartość - idealne do najszybszego odnajdowania danych
    po kluczu, nie trzeba stosować pętli przechodzącej po całym obiekcie
    słownikowym.
    {KLUCZ: wartość}

    
    Krotki - () lub bez - brak możliwości modyfikacji elementów. Najszybsze
    z reszty nad tym. Python rezerwuje tylko tyle miejsca, ile trzeba, brak
    funkcji / metod operowania na danych, usuwania, dodawania itp.

    
    Generatory - idealne do wielo terabajtowych danych, mamy dostęp do
    wygenerowanego elementu tylko w tym jednym momencie, nie możemy wracać
    do wcześniej wygenerowanych elementów. Można np. wyświetlić lub przekazać
    gdzieś indziej co chcemy, bo potem nie będzie odwołania do elementu.
'''
cardList = [    "9",     "9",     "9",     "9",
               "10",    "10",    "10",    "10",
             "Jack",  "Jack",  "Jack",  "Jack",
            "Queen", "Queen", "Queen", "Queen",
             "King",  "King",  "King",  "King",
              "Ace",   "Ace",   "Ace",   "Ace",
            "Joker", "Joker"]

print(cardList)

random.shuffle(cardList)

print("Przed wybraniem ostatniej karty: ")
print(cardList)
karta = cardList.pop() # .pop() - wybranie ostatniego elementu z listy.
print(karta)
print("Po wybraniu ostatniej karty: ")
print(cardList)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Wybranie kart, sample: ")
print(random.sample(cardList, 5))


print("Wybranie kart, sample, set: ")
print(random.sample(set(cardList), 5))
