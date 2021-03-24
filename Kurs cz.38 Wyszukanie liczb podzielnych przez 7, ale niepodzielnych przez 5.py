"""
    Liczby od 2 do 470 włącznie, które są:
    - podzielne przez 7
    - nie są podzielne przez 5

    Korzystamy z:
    - generatora
    - wyrażenia listowego
    - wyrażenia zbioru
    - wyrażenia słownikowego

    range(2, 471)

    7
    14
    21
    28
    35
    ```
    5
    10
    15
    20
    25
    30
    35
    ```

    7 % 7 == 0
    14 % 7 == 0
    21 % 7 == 0

    35 % 5 == 0
    ```

    modulo 7 == 0 i modulo 5 != 0

    ```
    
"""
# Generator
# Gdy chcemy liczby tylko wypisać / przepisać gdzieś indziej
# Nie można operować na wygenerowanych danych
#(

# )



# Wyrażenie listowe - gdy zależy nam na kolejności przechowywanych elementów

# Wyrażenie zbioru - operacje na zbiorach. Losowo wypisane elementy.

# Wyrażenie słownikowe - gdy zależy nam na funkcjonalności kluczy.

numbers = (
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
)

print("Generator: ")
for number in numbers:
    print(number)



numbers = [
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
]

print("Lista: ")
print(numbers)


numbers = {
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
}

print("Zbiór: ")
print(numbers)
