class BankAccount:
    bank_name = "BOG"

    def __init__(self, card_type, owner, balance):
        self.card_type = card_type
        self.owner = owner
        self.balance = balance

    def _minimum_balance(self):
        return 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < self._minimum_balance():
            raise ValueError("Balance is below the allowed minimum.")
        self.__balance = amount

    @balance.deleter
    def balance(self):
        del self.__balance
        print("Balance record deleted.")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def calculate_tax(amount):
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        return round(amount * 0.18, 2)


class SavingsAccount(BankAccount):
    def __init__(self, card_type, owner, balance, interest_rate=5):
        if interest_rate < 0:
            raise ValueError("Interest rate must be non-negative.")

        super().__init__(card_type, owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_fee = 2

    def apply_interest(self):
        interest = round(self.balance * self.interest_rate / 100, 2)
        self.balance += interest

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        super().withdraw(amount + self.withdrawal_fee)


class CreditAccount(BankAccount):
    def __init__(self, card_type, owner, balance, credit_limit=2000):
        if credit_limit < 0:
            raise ValueError("Credit limit must be non-negative.")

        self.credit_limit = credit_limit
        super().__init__(card_type, owner, balance)

    def _minimum_balance(self):
        return -self.credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        new_balance = self.balance - amount
        if new_balance < self._minimum_balance():
            raise ValueError("Credit limit exceeded.")

        self.balance = new_balance


account = BankAccount("Visa", "Lasha", 300)
account.deposit(200)
account.withdraw(150)
print(account.balance)  

savings = SavingsAccount("Visa", "Lasha", 1000)
savings.apply_interest()
print(savings.balance)  
savings.withdraw(100)
print(savings.balance) 
credit = CreditAccount("Mastercard", "Lasha", 100)
credit.withdraw(350)
print(credit.balance) 

print(BankAccount.get_bank_name())     
print(BankAccount.calculate_tax(100))  