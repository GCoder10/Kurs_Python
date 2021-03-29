import copy

def evil_function(toBeDestroyedList):
    print("Adres listy przed zmianą: ")
    print(id(toBeDestroyedList))
    toBeDestroyedList[0] = 108
    # toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

'''
print(myList)
#evil_function(tuple(myList))
print("evil_function(myList): ")
print(myList)
'''

"""
    tuple - krotka
    lista jako obiekt zmienny (mutable), nie można mieć gwarancji, że po wysłaniu
    listy jako argument do funkcji/metod/procedur nie zmieni się oryginalna
    zawartość.

    int, float itp - obiekty immutable - niezmienne - praca na kopiach wewnątrz
    funkcji/metod/procedur nie wpływa na oryginalne wartości.
"""
print("Adres listy przed wysłaniem do funkcji evil_function: ")
print(id(myList))
print(myList)
evil_function(myList)
print("evil_function(myList): ")
print(myList)
print("Adres listy po wysłaniu do funkcji evil_function: ")
print(id(myList))

myList = [1, 4, 2, 1, 52, 3]

print("Adres listy przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList))
print(myList)
evil_function(myList.copy()) # Metoda copy działająca na obiekcie. Stworzenie kopii
print("evil_function(myList.copy()): ")
print(myList)
print("Adres listy po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList))


print("\n\n\n\n\n\n\n\n\n\n\n\n")

# copy tworzy kopię, nowy obiekt, inny adres niż oryginał

'''
    ======================================================================
    copy - kopia płytka
    Poszczególne elementy kopiowanej listy nadal mają takie same adresy
    jak oryginał.

    Jednak te poszczególne elementy są tutaj jako int, czyli niezmienne,
    nie zmienimy teraz wartości oryginalnej listy.
'''
def evil_function2(toBeDestroyedList):
    print("Adres listy[0] przed zmianą: ")
    print(id(toBeDestroyedList[0]))
    print("Adres listy[2] przed zmianą: ")
    print(id(toBeDestroyedList[2]))
    print("Adres listy[4] przed zmianą: ")
    print(id(toBeDestroyedList[4]))
    print("====================================")
    toBeDestroyedList[0] = 108
    # toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

print("Adres listy[0] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[0]))
print("Adres listy[2] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[2]))
print("Adres listy[4] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[4]))
print("====================================")
print(myList)
evil_function2(myList.copy())
print("evil_function(myList.copy()): ")
print(myList)
print("Adres listy[0] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[0]))
print("Adres listy[2] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[2]))
print("Adres listy[4] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[4]))
print("====================================")
print("\n\n\n\n\n\n\n\n\n\n\n\n")



"""
    ======================================================================
    Jeżeli wewnątrz listy są obiekty mutable - zmienne, takie jak:
    listy, krotki, słownik, zbiór, generator
    to nastąpi zmiana wartości pomimo zastosowania copy
    Wtedy w zmienionym obiekcie zmieni się adres, ale tylko tam, reszta
    przed i po copy będzie miała takie same adresy.
"""
def evil_function3(toBeDestroyedList):
    print("Adres listy[0][0] przed zmianą: ")
    print(id(toBeDestroyedList[0][0]))
    print("Adres listy[2][1] przed zmianą: ")
    print(id(toBeDestroyedList[2][1]))
    print("Adres listy[1][0] przed zmianą: ")
    print(id(toBeDestroyedList[1][0]))
    print("====================================")
    toBeDestroyedList[0][0] = 108
    # toBeDestroyedList.clear()

myList = [[1, 4], [2, 1], [52, 3]]

print("Adres listy[0][0] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[0][0]))
print("Adres listy[2][1] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[2][1]))
print("Adres listy[1][0] przed wysłaniem do funkcji evil_function jako copy: ")
print(id(myList[1][0]))
print("====================================")
print(myList)
evil_function3(myList.copy())
print("evil_function(myList.copy()): ")
print(myList)
print("Adres listy[0][0] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[0][0]))
print("Adres listy[2][1] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[2][1]))
print("Adres listy[1][0] po wysłaniu do funkcji evil_function jako copy: ")
print(id(myList[1][0]))
print("====================================")
print("\n\n\n\n\n\n\n\n\n\n\n\n")





"""
    ======================================================================
    deepcopy - kopia głęboka, kopiowanie także
    wewnętrznych obiektów, więc nawet jeżeli są to obiekty
    mutable - zmienne, to nie nastąpi zmiana oryginału
    import copy

    Adresy wewnętrznych obiektów przed i po deepcopy nie różnią się.
"""
def evil_function4(toBeDestroyedList):
    print("Adres listy[0][0] przed zmianą: ")
    print(id(toBeDestroyedList[0][0]))
    print("Adres listy[2][1] przed zmianą: ")
    print(id(toBeDestroyedList[2][1]))
    print("Adres listy[1][0] przed zmianą: ")
    print(id(toBeDestroyedList[1][0]))
    print("====================================")
    toBeDestroyedList[0][0] = 108
    # toBeDestroyedList.clear()

myList = [[1, 4], [2, 1], [52, 3]]

print("Adres listy[0][0] przed wysłaniem do funkcji evil_function jako deepcopy: ")
print(id(myList[0][0]))
print("Adres listy[2][1] przed wysłaniem do funkcji evil_function jako deepcopy: ")
print(id(myList[2][1]))
print("Adres listy[1][0] przed wysłaniem do funkcji evil_function jako deepcopy: ")
print(id(myList[1][0]))
print("====================================")
print(myList)
evil_function4(copy.deepcopy(myList))
print("evil_function(myList.deepcopy()): ")
print(myList)
print("Adres listy[0][0] po wysłaniu do funkcji evil_function jako deepcopy: ")
print(id(myList[0][0]))
print("Adres listy[2][1] po wysłaniu do funkcji evil_function jako deepcopy: ")
print(id(myList[2][1]))
print("Adres listy[1][0] po wysłaniu do funkcji evil_function jako deepcopy: ")
print(id(myList[1][0]))
print("====================================")
print("\n\n\n\n\n\n\n\n\n\n\n\n")




'''
    ======================================================================
    copy - list()
    kopia płytka
'''
def evil_function5(toBeDestroyedList):
    print("Adres listy[0] przed zmianą: ")
    print(id(toBeDestroyedList[0]))
    print("Adres listy[2] przed zmianą: ")
    print(id(toBeDestroyedList[2]))
    print("Adres listy[4] przed zmianą: ")
    print(id(toBeDestroyedList[4]))
    print("====================================")
    toBeDestroyedList[0] = 108
    # toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

print("Adres listy[0] przed wysłaniem do funkcji evil_function jako list(myList): ")
print(id(myList[0]))
print("Adres listy[2] przed wysłaniem do funkcji evil_function jako list(myList): ")
print(id(myList[2]))
print("Adres listy[4] przed wysłaniem do funkcji evil_function jako list(myList): ")
print(id(myList[4]))
print("====================================")
print(myList)
evil_function5(list(myList))
print("evil_function(list(myList)): ")
print(myList)
print("Adres listy[0] po wysłaniu do funkcji evil_function jako list(myList): ")
print(id(myList[0]))
print("Adres listy[2] po wysłaniu do funkcji evil_function jako list(myList): ")
print(id(myList[2]))
print("Adres listy[4] po wysłaniu do funkcji evil_function jako list(myList): ")
print(id(myList[4]))
print("====================================")
print("\n\n\n\n\n\n\n\n\n\n\n\n")




'''
    ======================================================================
    copy - myList[:]
    kopia płytka
    myList[:] - wycięcie zawartości listy np.
    myList[0:4] od 0 elementu do 4
    myList[:] - od początku do końca
'''
def evil_function6(toBeDestroyedList):
    print("Adres listy[0] przed zmianą: ")
    print(id(toBeDestroyedList[0]))
    print("Adres listy[2] przed zmianą: ")
    print(id(toBeDestroyedList[2]))
    print("Adres listy[4] przed zmianą: ")
    print(id(toBeDestroyedList[4]))
    print("====================================")
    toBeDestroyedList[0] = 108
    # toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

print("Adres listy[0] przed wysłaniem do funkcji evil_function jako myList[:] ")
print(id(myList[0]))
print("Adres listy[2] przed wysłaniem do funkcji evil_function jako myList[:] ")
print(id(myList[2]))
print("Adres listy[4] przed wysłaniem do funkcji evil_function jako myList[:] ")
print(id(myList[4]))
print("====================================")
print(myList)
evil_function6(myList[:])
print("evil_function(myList[:]): ")
print(myList)
print("Adres listy[0] po wysłaniu do funkcji evil_function jako myList[:] ")
print(id(myList[0]))
print("Adres listy[2] po wysłaniu do funkcji evil_function jako myList[:] ")
print(id(myList[2]))
print("Adres listy[4] po wysłaniu do funkcji evil_function jako myList[:] ")
print(id(myList[4]))
print("====================================")
print("\n\n\n\n\n\n\n\n\n\n\n\n")
