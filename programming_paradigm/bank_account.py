class BankAccount:
    __amount = 0

    def __init__(self, amount):
        self.__amount = amount

    def deposit(self, deposit_amount):
        self.__amount += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.__amount > withdraw_amount:
            self.__amount -= withdraw_amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(self.__amount)
