from Kurs_cz_128_Dziedziczenie_i_nadpisywanie_metod_super import BankAccount, MinimumBalanceAccount, MinimumBalanceAccountWithInheritance

'''
   Dziedziczenie, to samo co było w C++/C++11, ta sama logika.
W C++/C++11 dziedziczenie różne w zależności od rodzaju zmiennych,
metod w klasie dziedziczonej przez inną klasę, public, protected, private
Klasa niżej położona - subklasa


    Dziedziczenie po to, aby nie było sytuacji, w których trzeba 
    zmieniać te same rzeczy w 90% podobnych klasach, których może
    być wiele dziesiąt i więcej.
'''

accountMin = MinimumBalanceAccount(1500,1000)
result = accountMin.try_withdraw_with_result_class(800) # 1500 - 800 < 1000, False
"""
Klasa MinimumBalanceAccount
metoda try_withdraw_with_result_class
Spr. czy nie przekroczymy ustalonego minimalnego bilansu dla 
konta po wypłaceniu określonej ilości pieniędzy,
self.balance -> bilans dla konkretnej instancji klasy/obiektu, tutaj: accountMin
amount -> parametr przekazywany do metody try_withdraw_with_result_class 
self.minimumBalance -> minimalny do osiągnięcia bilans konta po 
wypłaceniu pieniędzy dla konkretnej instancji klasy/obiektu, tutaj: accountMin
    if (self.balance - amount > self.minimumBalance):
"""
print("result.isSuccess",result.isSuccess)
print("result.message",result.message)
print("result.value",result.value)
print("\n")


result = accountMin.try_withdraw_with_result_class(400) 
print("result.isSuccess",result.isSuccess)
print("result.message",result.message)
print("result.value",result.value)


"""
    MinimumBalanceAccountWithInheritance
    Klasa, która dziedziczy metody z klasy BankAccount
    W klasie dziedziczącej możemy nadpisać sposób działania
    metod.
    Nadpisywanie działania metod.
    Jeżeli w klasie dziedziczącej nie będzie metody, która
    jest w klasie rodzic i ta metoda zostanie wywołana z klasy
    dziecko, to ostatecznie zostanie wywołana metoda z klasy rodzic
    z powodu jej braku w klasie dziecko.
"""
print("\n\n\n\n\n\n")
accountMinWithInheritance = MinimumBalanceAccountWithInheritance(1500,1000)
result = accountMinWithInheritance.try_withdraw_with_result_class(800)
print("result.isSuccess",result.isSuccess)
print("result.message",result.message)
print("result.value",result.value)
print("\n")


result = accountMinWithInheritance.try_withdraw_with_result_class(400) 
print("result.isSuccess",result.isSuccess)
print("result.message",result.message)
print("result.value",result.value)


"""
    Można też w metodzie w klasie dziecko korzystać częściowo 
    tak samo jak w klasie rodzic, przykład w metodzie __init__
    w klasie MinimumBalanceAccountWithInheritance
"""
'''
    Wykorzystanie metody super(), nie trzeba dawać w parametrach
    self, bo od razu wysyła "siebie".
    Od razu automatycznie wysyła parametry do klasy wyżej położonej
    (z perspektywy dziedziczenia).
'''
"""
    Klasa: MinimumBalanceAccountWithInheritance
    Metoda: try_withdraw_with_result_class

    return super().try_withdraw_with_result_class(amount)
    Zwracamy to, co zostało wykonane w metodzie z klasy 
    wyżej po wcześniejszym przekazaniu tam parametrów i self
    "siebie" przez metodę super().
"""
