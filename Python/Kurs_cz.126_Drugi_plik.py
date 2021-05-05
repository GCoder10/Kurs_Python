from Kurs_cz_126_Konto_bankowe_Wyplacanie_Wplacanie import BankAccount


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
account.withdraw(200)
account.withdraw(2500)

# Zastosowanie metody dunder - double underscore, str, w celu 
# zwrócenia aktualnego bilansu na koncie względem konkretnej
# instancji klasy, obiektu.
print(account)
print("\n\n\n\n\n\n\n\n\n\n")
account2 = BankAccount(10000)
account2.withdraw(100000)
account2.withdraw(5500)
account2.deposit(600)
print("5100:")
print(account2)