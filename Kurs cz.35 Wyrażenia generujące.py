import sys

evenNumbers = [element
               for element in range(400)
               if (element % 2 == 0)]

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0))


# Lista [], krotki () lub bez, słownik {klucz:wartość}, zbiór {}.
print(evenNumbers)


# Obiekt - generator. 
print(evenNumbersGenerator)

"""
    Generator zajmuje tylko troszeczkę miejsca w pamięci, natomiast lista
    zabrała od razu ilość pamięci potrzebną na wszystkie elementy.

    Np. kilka terabajtów danych, czasami trzeba generator właśnie.
"""

print("Ilość miejsca zajętego przez liste: ")
print(sys.getsizeof(evenNumbers))

print("Ilość miejsca zajętego przez generator: ")
print(sys.getsizeof(evenNumbersGenerator))

'''
    Generator może być argumentem dla jakiejś funkcji.
'''
print("sum(evenNumbersGenerator): ")
print(sum(evenNumbersGenerator))


# Dostanie się do elementów zawartych w generatorze.
# Element nie jest zapisywany w pamięci.
for item in evenNumbersGenerator:
    print(item)

print("Ilość miejsca zajętego przez generator po wygenerowaniu elementów: ")
print(sys.getsizeof(evenNumbersGenerator))



'''
    plik txt 3 terabajty
    Generatory - tracimy właściwości swobodnego operowania na elementach.
    Generowanie rekordów z pliku txt, gdy potrzebujemy.
    Nie możemy wrócić do wygenerowanych elementów.

    Generatory są idealne właśnie w przypadkach konieczności operowania na
    bardzo dużych danych, dosłownie terabajtach.
'''
