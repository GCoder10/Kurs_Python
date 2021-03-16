wynik = 0 # 0 jest neutralne w dodawaniu.

i = 0
while i < 4:
    x = int(input("Podaj liczbe: ")) # Rzutowanie wprowadzanych danych na int.
# Bez rzutowania dane z funkcji input() są zwracane jako char, ciąg znaków.
    wynik += x
    i += 1
print("Wynik dodawania liczb to:",wynik)
# Ciało pętli - instrukcje z wzcięciem.
