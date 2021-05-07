from Kurs_cz_127_Obsluga_zwracanych_wartosci_z_wyplacania import BankAccount


account = BankAccount()

# Depozyt - wpłacenie pieniędzy
account.deposit(500)


# Withdraw - wypłacanie pieniędzy. 
'''
        def withdraw(self, amount):
            if (self.balance > amount):
                self.balance -= amount
    Jeżeli wypłacana kwota z konta jest mniejsza od 
    bilansu na koncie względem konkretnej instancji klasy, obiektu 
    (self), to wypłacenie i pomniejszenie ogólnego bilansu dla tego
    obiektu o podaną kwotę.
'''
account.try_withdraw(200)
account.try_withdraw(2500)

# Zastosowanie metody dunder - double underscore, str, w celu 
# zwrócenia aktualnego bilansu na koncie względem konkretnej
# instancji klasy, obiektu.
'''
    Najprostsza walidacja danych,
    return True/False w metodzie i obsługa tego w kodzie.
    Sposoby w metodzie try_withdraw:
        1. bool, True, False, obsługa tego
        2. pisanie komunikatów w metodzie
        3. łączenie komunikatów z return True/False
        4. Zwrócone trzy wartości z metody: bool, str, int,
        odebranie tego i obsłużenie
        5. Zwrócone trzy wartości z metody: bool, str, int jako
        krotka (tuple), odebranie tego i obsłużenie
        Nie trzeba teraz pilnować kolejności przyjmowanych
        argumentów z metody. 
        6. Zwrócone trzy wartości z metody: bool, str, int jako
        słownik (dict), przypisanie do kluczy odpowiednich wartości,
        szukanie interesującej wartości ze zwróconej całości słownika
        po kluczach.
        7. Używanie klasy Result do rezultatów z metody.
        Korzystanie z klasy daje plus podpowiedzi w np. VSC jak 
        napiszemy result.
'''
print(account)
print("\n\n\n\n\n\n\n\n\n\n")
account2 = BankAccount(10000)


if(account2.try_withdraw(100000)):
    print("Wypłacono")
else:
    print("Za mało pieniędzy na koncie")


if(account2.try_withdraw(5500)):
    print("Wypłacono")
else:
    print("Za mało pieniędzy na koncie")


account2.deposit(600)
print("5100:")
print(account2)
print("\n\n\n\n\n\n\n\n\n\n")

isSuccess, message, value = account2.try_withdraw(100000)
print("isSuccess",isSuccess)
print("message",message)
print("value",value)


print("\n\n\n\n\n\n\n\n\n\n")
result = account2.try_withdraw_with_tuple(500)
print("result[0] isSuccess",result[0])
print("result[1] message",result[1])
print("result[2] value",result[2])



print("\n\n\n\n\n\n\n\n\n\n")
result = account2.try_withdraw_with_dict(500)
print("result['isSuccess'] isSuccess",result["isSuccess"])
print("result['message'] message",result["message"])
print("result['value'] value",result["value"])
print("\n")
if (result["isSuccess"]):
    print(result["message"])
    print(result["value"])



print("\n\n\n\n\n\n\n\n\n\n")
result = account2.try_withdraw_with_result_class(500)
if (result.isSuccess):
    print(result.message)
    print(result.value)
else:
    print("Nie udało się")