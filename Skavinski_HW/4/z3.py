import random

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = None  # временно, чтобы вызвать сеттер
        self.balance = initial_balance  # проверка через сеттер

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.__balance = value

    @property
    def account_number(self):
        return self.__account_number

    @staticmethod
    def generate_account_number():
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    @classmethod
    def create_account(cls, initial_balance):
        account_number = cls.generate_account_number()
        return cls(account_number, initial_balance)


# Пример использования
account = BankAccount.create_account(1000)
print("Account Number:", account.account_number)
print("Balance:", account.balance)

# Попытка установить отрицательный баланс
try:
    account.balance = -500
except ValueError as e:
    print("Ошибка:", e)