"""
Automatyczne formatowanie kodu, ustawianie wszelkich spacji,
enterów, odstępów itp. automatycznie.


CTRL + SHIFT + P
format document
Instalacja autopep8
Potem jeszcze raz:
CTRL + SHIFT + P
format document
Albo:
SHIFT + ALT + F




Automatyczne formatowanie podczas zapisu pliku:
CTRL + , (Settings)
format save
Zaznaczenie box'a pod 'Format On Save'



Opcje Auto Save i Format On Save nie łączą się,
plik nie będzie formatowany podczas automatycznego
zapisu, tylko podczas ręcznego.
"""
listOfNumbers = [1, 4, 20, 20, 45]
for number in listOfNumbers:
    print(number)


def sample(a, b, c):
    print(a)


.car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car.update({'color': 'White'})
print(car)