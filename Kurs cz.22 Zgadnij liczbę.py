'''
    Użytkownik podaje liczbę.
    Program sprawdza, czy podana liczba zgadza się z tą sekretną.
'''
szukanaLiczba = 40
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Odgadnij liczbę: "))
    if (zgadywanaLiczba > szukanaLiczba):
        print("Podano za dużą liczbę")
    elif (zgadywanaLiczba < szukanaLiczba):
        print("Podano za małą liczbę")
    else:
        print("Zgadłeś")
