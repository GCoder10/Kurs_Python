"""
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Start number: 0
    1
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 1
    [number_multiplied_by_itself_generator()] Start number: 1
    4
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 2
    [number_multiplied_by_itself_generator()] Start number: 2
    9
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 3
    [number_multiplied_by_itself_generator()] Start number: 3
    16
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 4
    [number_multiplied_by_itself_generator()] Start number: 4
    25

    Pierwsze wywołanie funkcji generującej, powiększenie liczby o 1, zapisanie stanu funkcji, jej zmiennych itd.
    Drugie wywołanie, przed dodaniem 1, potem zwraca 4 bo 2*2
    Trzecie wywołanie, startowa wartość już 3, 3*3=9
    W każdym momencie można wrócić do wartości przechowywanych przez funkcję generującą.
"""
'''
    Będzie się wyświetlało w sample, None, za każdym wywołaniem.
    Można wrócić do miejsca, które już zostało zwrócone przez generator, trzeba użyć do tego metody send.
        def number_multiplied_by_itself_generator():
            number = 0
            while True:
                print("[number_multiplied_by_itself_generator()] Start number:", number)
                number = number + 1
                sample = yield number * number
                print("[number_multiplied_by_itself_generator()] Po yield number:", number)
                print("[number_multiplied_by_itself_generator()] Po yield sample:", sample)

    Można zmienić za pomocą metody send dokładnie tą część kodu:
        yield number * number

    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Start number: 0
    1
    >>> numberGenerator.send(40)
    [number_multiplied_by_itself_generator()] Po yield number: 1
    [number_multiplied_by_itself_generator()] Po yield sample: 40
    [number_multiplied_by_itself_generator()] Start number: 1
    4
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 2
    [number_multiplied_by_itself_generator()] Po yield sample: None
    [number_multiplied_by_itself_generator()] Start number: 2
    9
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 3
    [number_multiplied_by_itself_generator()] Po yield sample: None
    [number_multiplied_by_itself_generator()] Start number: 3
    16
    >>> numberGenerator.send(140)
    [number_multiplied_by_itself_generator()] Po yield number: 4
    [number_multiplied_by_itself_generator()] Po yield sample: 140
    [number_multiplied_by_itself_generator()] Start number: 4
    25
    >>> next(numberGenerator)
    [number_multiplied_by_itself_generator()] Po yield number: 5
    [number_multiplied_by_itself_generator()] Po yield sample: None
    [number_multiplied_by_itself_generator()] Start number: 5
    36

    Taka zmiana nie wpływa na zwracane wartości z funkcji generującej, zamiast:
    yield number * number już jest wartość np. 40 lub 140 zamiast None po
    wygenerowaniu.
'''
"""
    def number_multiplied_by_itself_generator():
        number = 0
        while True:
            print("[number_multiplied_by_itself_generator()] Start number:", number)
            number = number + 1
            number = yield number * number
            print("[number_multiplied_by_itself_generator()] Po yield number:", number)

    1. next(numberGenerator) --> Uruchomienie tego generatora
    2. numberGenerator.send(20) --> Zastąpienie wartości pod yield już na 20
    

        >>> next(numberGenerator)
        [number_multiplied_by_itself_generator()] Start number: 0
        1
        >>> numberGenerator.send(20)
        [number_multiplied_by_itself_generator()] Po yield number: 20
        [number_multiplied_by_itself_generator()] Start number: 20
        441

    start number = 20, powiększenie o 1, 21*21=441

    Potem znowu można skoczyć do innej wartości w generatorze, odpowiednio zastępując wartości będące pod
    yield za pomocą metody send:
        >>> next(numberGenerator)
        [number_multiplied_by_itself_generator()] Start number: 0
        1
        >>> numberGenerator.send(20)
        [number_multiplied_by_itself_generator()] Po yield number: 20
        [number_multiplied_by_itself_generator()] Start number: 20
        441
        >>> numberGenerator.send(2)
        [number_multiplied_by_itself_generator()] Po yield number: 2
        [number_multiplied_by_itself_generator()] Start number: 2
        9
    start number = 2, powiększenie o 1, 3*3=9
"""
'''
    Co się stanie, jeżeli nie uruchomimy generatora, tylko od razu send:
        >>> numberGenerator.send(2)
        Traceback (most recent call last):
          File "<pyshell#53>", line 1, in <module>
            numberGenerator.send(2)
        TypeError: can't send non-None value to a just-started generator
    Są dwa sposoby rozpoczęcia pracy generatora:
        1. next(numberGenerator)
        2. numberGenerator.send(None)
'''
def number_multiplied_by_itself_generator():
    number = 0
    while True:
        print("[number_multiplied_by_itself_generator()] Start number:", number)
        #number = number + 1
        number = yield number * number
        print("[number_multiplied_by_itself_generator()] Po yield number:", number)
generatedNumbers = []
        
numberGenerator = number_multiplied_by_itself_generator()
numberGenerator.send(None)
# Sami teraz wybieramy, jaka wartość to start.
# Od 0 do 20 i potem od 30 do 50
for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))


print("Lista zawierająca 20 wygenerowanych liczb z funkcji generującej: ")
print(generatedNumbers)


for i in range(30, 50):
    generatedNumbers.append(numberGenerator.send(i))


print("Lista zawierająca wygenerowanych kolejnych 30 liczb z funkcji generującej (razem 50 liczb w liście): ")
print(generatedNumbers)

