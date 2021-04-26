"""
    VSC -> Extensions -> Python Preview by Dongli

    Po prawej na górze jest teraz:
    Obok 'Play':
    Open Preview to the Side



    Ładnie widać, co się teraz dzieje, co się działo
    w funkcji podziel, jakie w zasięgu globalnym,
    Można interaktywnie cofać się w instrukcjach, 
    przemieszczać się dowolnie po wykonanym programie.


    Wskazywanie poprzez strzałki, co zostało wykonane
    a co zostanie wykonane w następnym kroku.

    Można na bieżąco edytować kod i widzieć zmiany
    w Python Preview.
    Na bieżąco pokazuje błędy wtedy, blokuje wykonanie.



    Pewne rzeczy też nie działają np. input
    'User input is not supported'
"""
def podziel(a, b):
    if (b == 0):
        return
    print("aaa")
    return a / b


x = podziel(10,5)
if (x):
    print("Podzielono poprawnie", x)
else:
    print("Coś poszło nie tak")

print("cośCoś")