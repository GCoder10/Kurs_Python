"""
    break - przerwanie wykonywania instrukcji, np. w pętli.

    continue - anulowana jest dana iteracja pętli. Kontynuowanie pracy pętli,
    następne jej kroki (iteracje).
"""

wynik = 0
for i in range(3):
    x = int(input("Podaj dodatnią liczbe: "))
    if (x > 0):
        wynik += x
    else:
        print("Liczba musi być dodatnia.")
        break
print("Wynik dodawania liczb to:",wynik)



wynik = 0
for i in range(3):
    x = int(input("Podaj dodatnią liczbe: "))
    if (x > 0):
        wynik += x
    else:
        print("Liczba musi być dodatnia.")
        continue
print("Wynik dodawania liczb to:",wynik)



'''
    continue spowoduje, że wszystkie pozostałe instrukcje w danej
    iteracji pętli nie wykonają się a tym samym nie zostanie zwiększony
    licznik i.
    Liczby podawane do momentu uzyskania 3 dodatnich.
'''
wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbe: "))
    if (x > 0):
        wynik += x
    else:
        print("Liczba musi być dodatnia.")
        continue
    i += 1
print("Wynik dodawania liczb to:",wynik)
