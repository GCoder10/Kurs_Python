"""
Automatyczne uzupełnianie kodu poprzez wstawianie
gotowych szablonów.

for, wybieramy for z opcją 'Code snippet for a for loop (Python)'
Po lewej od for będzie pusty kwadracik.
Klikamy TAB.
Uzupełnianie szablonu:
wpisujemy wartość i przejście dalej to TAB i przeskakujemy
po miejscach w szablonie dalej po jego elementach.


Jeżeli nie działa od razu, to:
Extensions --> python snippets by Ferhat Yalcin



CTRL + SHIFT + P
Insert Snippet
Wyświetlą się te, które są do dyspozycji.



Po wybraniu np. pętli if, TAB, i dalej można TAB'ować,
będziemy przeskakiwać po szablonach.


Teraz TAB'owanie = przechodzenie dalej w szablonach od
tego, który wpisaliśmy jako pierwszy.


Można tak tworzyć szybko np. wyrażenie listowe:
list.comp=>_1
x = [i for i in range(10)]
print(x)

lub:
list.comp=>_4
listOfWords = ['this','is','a','list','of','words']
items = [ word[0] for word in listOfWords ]
print(items)

Lub jakieś gotowe szablony dla słowników:

dictionary.setdefault=>
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.setdefault('color', 'white')
print(x)

"""
listOfNumbers = [1, 4, 20, 20, 45]

for number in listOfNumbers:
    print(number)

for number in listOfNumbers:
    #pass <-- pominięcie kodu, passowanie, pomijanie na ten moment.
    print(number)
