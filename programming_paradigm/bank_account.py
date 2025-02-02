class BankAccount:
    __amount = 0

    def __init__(self, amount):
        self.__amount = amount

    def deposit(self, deposit_amount):
        self.__amount += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.__amount > withdraw_amount:
            self.__amount -= withdraw_amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${float(self.__amount):.2f}")


# bank = BankAccount(100)
# bank.withdraw(150)
# bank.display_balance()
