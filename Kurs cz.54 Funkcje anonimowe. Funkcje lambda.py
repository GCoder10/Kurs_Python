"""
    Funkcje bez nazwy
    Funkcje inline - najszybciej się kompilują
    To samo dotyczy C/C++/C++11
    Tam też są funkcje inline, które właśnie kompilują się najszybciej.
"""
def podwoj(x):
    return x * 2

def podobne_do_filter(x):
    if (x % 2) == 0:
        return x

test = lambda x: x * 2

print("podwoj(4): ")
print(podwoj(4))

print("test(4): ")
print(test(4))


print("(lambda x: x * 2)(4)")
print((lambda x: x * 2)(4))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

'''
    filter() przyjmuje jako pierwszy parametr funkcję, filtrowanie
    względem funkcji, jaka zostanie przekazana.
    Przykładowe zastosowanie funkcji lambda, anonimowej.

    Filter zwraca obiekt filtrujący, który trzeba jeszcze zamienić na
    listę. 
'''
my_list = [2, 14, 22, 7, 6, 4, 5, 17]
my_filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print("[filter(lambda x: x % 2 == 0, my_list)] my_filtered_list: ")
print(my_filtered_list)


my_filtered_list2 = list(filter(podobne_do_filter, my_list))
print("[filter(podobne_do_filter, my_list)] my_filtered_list: ")
print(my_filtered_list2)


# Wyrażenie listowe
my_filtered_list3 = [x for x in my_list if(x % 2) == 0]
print("[x for x in my_list if(x % 2) == 0]: ")
print(my_filtered_list3)
