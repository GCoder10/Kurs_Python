"""
    Python Quick Print to rozszerzenie:

    VSC -> Extensions -> Python Quick Print by AhadCove

    Zmiana skrótu do użycia PQP, tak samo dla czegokolwiek 
    innego można zmieniać skróty:

    VSC -> Keyboard Shortcuts -> print python selection

    Tutaj: zaznaczamy samo 'x' w x = divide(20, 5)
    i klikamy: CTRL + SHIFT + L i od razu otrzymujemy:
    print('x: ', x)
"""

def divide(a, b):
    if (b == 0):
        return

    return a / b


x = divide(20, 5)
print('x: ', x)