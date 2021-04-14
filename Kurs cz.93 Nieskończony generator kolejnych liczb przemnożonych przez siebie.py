"""
    Funkcja generująca w nieskończoność kolejne liczby przemnożone przez siebie,
    tzn.:
        1    1*1 = 1
        4    2*2 = 4
        9    3*3 = 9
        16   4*4 = 16
        25   5*5 = 25
        36   6*6 = 36

    Skorzystanie z funkcji generującej 20 elementów, po czym wrócenie od
    momentu skończenia i wygenerowanie następnych 20 liczb.

    Zapisanie wygenerowanych elementów w tej samej liście.
"""
'''
    Dopóki prawda, czyli w nieskończoność:
        def number_multiplied_by_itself_generator():
            number = 0
            while True:
                number = number + 1
                yield number * number
    Zwiększanie liczby o jeden i zwracanie przemnożonej liczby przez samą siebie.
'''
"""
    Dzięki temu, że stan funkcji generującej, jej zmienne, wartości itp. są przechowywane w czasie działania
    programu, można wrócić do niej w każdej chwili i zacząć od miejsca, gdzie się skończyło, np. tutaj
    wygenerownie kolejnych 30 liczb po tym, jak już wygenerowaliśmy 20.
        for k in range(30):
            generatedNumbers.append(next(numberGenerator))
    i dopisanie do już istniejącej listy:
            generatedNumbers.append(next(numberGenerator))
"""
'''
    W przypadku tego kodu jest coś takiego jak zmienna nieużyta k, można to zaznaczyć używając zamiast k: _
''' 
def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number
generatedNumbers = []
        
numberGenerator = number_multiplied_by_itself_generator()

for k in range(20):
    generatedNumbers.append(next(numberGenerator))


print("Lista zawierająca 20 wygenerowanych liczb z funkcji generującej: ")
print(generatedNumbers)


for _ in range(30):
    generatedNumbers.append(next(numberGenerator))


print("Lista zawierająca wygenerowanych kolejnych 30 liczb z funkcji generującej (razem 50 liczb w liście): ")
print(generatedNumbers)
