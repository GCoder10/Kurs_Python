"""
    yield - z ang. dostarczyć, dać, wydać z siebie.
    Wartości są generowane tylko w monencie, gdy chcemy.
    Właściwości generatorów:
        Dostęp do danych tylko w momencie generacji, nie mamy dostępu do n-1 i wszystkich
        poprzednich elementów.
        Więc jeżeli chcemy jakoś wykorzystać dane generowane przez generator, to tylko
        w momencie ich wygenerowania, np. w celu wyświetlenia bądź przekazania gdzieś indziej,
        jeżeli dodatkowo np. spełniają jakieś odpowiednie warunki.
        Idealny sposób na operowanie na np. wielo terabajtowych danych przy jednoczesnym
        minimalnym zajmowaniu miejsca w pamięci przez generator, nie ważne jak duży jest plik
        generator będzie generował dane w oparciu o jakiś np. wzór, pattern na podstawie takiego
        pliku i zawsze będzie zajmował tak samo mało miejsca, ale w zamian właśnie nie są
        przechowywane nigdzie wszystkie wcześniej wygenerowane elementy.
"""
"""
    Funkcja generująca, bez generatora, liczby parzyste,
    jeżeli element z którejś z liczb z 400 jest podzielny przez 2 (modulo 2 == 0, reszta z
    dzielenia == 0), to zwracanie elementu.
        def generate_even_numbers():
            for element in range(400):
                if (element % 2) == 0:
                    return element

    a = generate_even_numbers()
    ale wtedy zawsze a zwróci 0.
    return == zakończenie funkcji, od nowa znowu dlatego zwraca 0.

    A chodzi o uzyskanie efektu, że jak ponownie się odwołamy do funkcji, to żeby zwróciła
    kolejną wartość a nie się od razu po zwróceniu wartości zakańczała.

        def generate_even_numbers():
            for element in range(400):
                if (element % 2) == 0:
                    yield element
    Teraz po a następuje komunikat o stworzeniu generatora, a dokładniej iteratora, obiektu,
    po którym można przechodzić, w sumie to jak w C++/C++11 kontenery, vectory, STL. Tam też
    do vectorów trzeba używać iteratorów, czyli obiektów, dzięki którym można przechodzić po
    wartościach przechowywanych w vectorze.
    <generator object generate_even_numbers at 0x000002251209ED60>
    Czyli może to oznaczać, że wartości nie są przechowywane jak w przypadku tablic, tablic z
    pamięcią dynamicznie alokowaną (new int itp.) obok siebie w bloku w pamięci, tylko mogą
    być w różnych miejscach w pamięci, dlatego potrzebny jest specjalny obiekt taki jak
    iterator, który będzie "wiedział, znał" adresy tych zmiennych.

    a teraz zawiera generator.
    next(a)
    Następny element wygenerowany przez generator, next przechodzi po tych elementach,
    zachowuje się jak iterator.
"""
'''
    return --> Funkcja, Python podczas startu programu wejdzie do tej funkcji.
    yield --> Funkcja generująca, Python podczas startu programu nie wejdzie do tej funkcji.
    a = generate_even_numbers() --> Stworzenie generatora i przypisanie go do zmiennej a.
    Tylko pierwsze wywołanie zmiennej next(a) wywoła instrukcje na starcie funkcji generującej, potem
    potem już tylko po yield i przed:
        >>> a
        <generator object generate_even_numbers at 0x00000171B7C8ED60>
        >>> next(a)
        [generate_even_numbers()] Start
        [generate_even_numbers()] Przed yield
        0
        >>> next(a)
        [generate_even_numbers()] Po yield
        [generate_even_numbers()] Przed yield
        [generate_even_numbers()] Przed yield
        2
        >>> next(a)
        [generate_even_numbers()] Po yield
        [generate_even_numbers()] Przed yield
        [generate_even_numbers()] Przed yield
        4
        >>> next(a)
        [generate_even_numbers()] Po yield
        [generate_even_numbers()] Przed yield
        [generate_even_numbers()] Przed yield
        6
    Czyli stan funkcji generującej jest ciągle gdzieś utrzymywany, można zawsze wrócić do niej. 
'''
"""
    generate_10_numbers(): Funkcja generująca 10 liczb po kolei i po każdym wywołaniu
    podniesienie wartości zmiennej x o 1
    Stan funkcji generującej jest gdzieś utrzymywany, więc wartość x jest ciągle dostępna,
    można na niej operować po zwróceniu któregoś x z kolei.
    Zamienienie wygenerowanych tak liczb na listę:
        print(list(generate_10_numbers()))
"""
'''
    Funkcja generująca będzie dużo prostsza i bardziej praktyczna niż: 

    evenNumbersGenerator = (
                            element
                            for element in range(400)
                            if (element % 2 == 0)
                        )
    Lub

    generate_10_numbers_expression = (
                                         x
                                         for x in range(10)
                                     )

    Generator stworzony w sposób podany powyżej nie będzie mógł zostać wywołany
    drugi i kolejny raz jak funkcja generująca.

        list(generate_10_numbers()): 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list(generate_10_numbers()): 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list(generate_10_numbers()): 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list(generate_10_numbers_expression): 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list(generate_10_numbers_expression): 
        []
        list(generate_10_numbers_expression): 
        []
        list(generate_10_numbers_expression): 
        []
'''
"""
    Funkcje generujące będą super w przypadku właśnie danych, które bardzo dużo zajmują miejsca,
    zaczynamy, zakańczamy gdzie chcemy, generowanie wartości na bieżąco.
"""
def generate_even_numbers():
    print("[generate_even_numbers()] Start")
    for element in range(400):
        print("[generate_even_numbers()] Przed yield")
        if (element % 2) == 0:
            yield element
            print("[generate_even_numbers()] Po yield")


evenNumbersGenerator = (
                            element
                            for element in range(400)
                            if (element % 2 == 0)
                        )

a = generate_even_numbers()

def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1
print("list(generate_10_numbers()): ")
print(list(generate_10_numbers()))
print("list(generate_10_numbers()): ")
print(list(generate_10_numbers()))
print("list(generate_10_numbers()): ")
print(list(generate_10_numbers()))


generate_10_numbers_expression = (
                                     x
                                     for x in range(10)
                                 )


print("list(generate_10_numbers_expression): ")
print(list(generate_10_numbers_expression))
print("list(generate_10_numbers_expression): ")
print(list(generate_10_numbers_expression))
print("list(generate_10_numbers_expression): ")
print(list(generate_10_numbers_expression))
print("list(generate_10_numbers_expression): ")
print(list(generate_10_numbers_expression))
