"""
    Argumenty kluczowe i pozycyjne
    kluczowy - w postaci: klucz - wartość (domyślny)
    pozycyjne - takich, w których liczy się kolejność przy wywołaniu
"""

def greet(name, message):
    print(message, name)

# Dzięki temu nie trzeba pilnować kolejności przesyłanych argumentów do funkcji.
greet(name = "Imie", message = "Witaj")


greet(message = "Witaj", name = "Imie")


# sep - separator, domyślnie spacja
def greet2(name, message):
    print(message, name, sep = " @! \n #$ ")


greet2(message = "Witaj", name = "Imie")


def greet3(name, message, seperator = " "):
    print(message, name, sep = seperator)


greet3(message = "[Domyślnie spacja] Witaj", name = "Imie")
greet3(message = "[Sep: () ] Witaj", name = "Imie", seperator = " () ")


def greet4(name, message = "Co tam", seperator = " "):
    print(message, name, sep = seperator)

    
greet4("Przykładowe imie", seperator = " \n ")


greet4("Przykładowe imie", seperator = " \n ", message = "Przykładowa wiadomość")
