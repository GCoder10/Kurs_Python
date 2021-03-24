"""
    Funkcja - blok kodu do którego można odwołać się w każdej chwili, aby
    otrzymać pożądany przez nas wynik.

    def - definition

    def nazwa_funkcji():
        instrukcja1
        instrukcja2


    nazwa_funkcji()
"""
def wiadomosc_powitalna(imie):
    print("test funkcji wiadomosc_powitalna()")
    print("test funkcji wiadomosc_powitalna() 2")
    print(imie, "cześć")

print("Powitanie użytkownika programu 1")
print("Powitanie użytkownika programu 2")
wiadomosc_powitalna("imiePrzykładowe1")
print("Powitanie użytkownika programu 3")
wiadomosc_powitalna("imiePrzykładowe2")


wiadomosc_powitalna("imiePrzykładowe3")


imiona = ["Imie1", "Imie2", "SuperImiePrzykładowe3", "coś4"]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Przekazywanie parametrów, argumentów z listy do funkcji: ")
for imie in imiona:
    wiadomosc_powitalna(imie)
    
