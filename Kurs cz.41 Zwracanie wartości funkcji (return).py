"""
    return - zwrócić
    None - nic, false
"""

def pole_prostokata(a, b):
    # print(a * b)
    return a * b

print("print(pole_prostokata(2, 8)): ")
print(pole_prostokata(2, 8))


print("print(5 * pole_prostokata(2, 8)): ")
print(5 * pole_prostokata(2, 8))


poleProstokataA = pole_prostokata(2, 8)
print("print(5 * poleProstokataA): ")
print(5 * poleProstokataA)





poleProstokataB = pole_prostokata(24, 2)
print("print(5 * poleProstokataB): ")
print(5 * poleProstokataB)
print("\n\n\n\n\n\n\n\n\n\n\n")

def dzielenie(a, b):
    if (b == 0):
        return "Nie dziel przez zero"
    print("TEST")
    return a/b

print("Dzielenie 10/0: ")
print(dzielenie(10,0))

print("Dzielenie 10/2: ")
print(dzielenie(10,2))

print("\n\n\n\n\n\n\n\n\n\n\n")

def dzielenie(a, b):
    if (b == 0):
        return
    print("TEST")
    return a/b

print("Dzielenie 10/0: ")
print(dzielenie(10,0))

print("Dzielenie 10/2: ")
print(dzielenie(10,2))

print("\n\n\n\n\n\n\n\n\n\n\n")

print("if z None")
if (dzielenie(9,0)):
    print("Podzielono.")
else:
    print("Nie podzielono")

print("if bez None")
if (dzielenie(9,1)):
    print("Podzielono.")
else:
    print("Nie podzielono")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
x1 = dzielenie(9,0)
x2 = dzielenie(9,1)
print("if z None")
if (x1):
    print("Podzielono.")
else:
    print("Nie podzielono")

print("if bez None")
if (x2):
    print("Podzielono.")
else:
    print("Nie podzielono")
