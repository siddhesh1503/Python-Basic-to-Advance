from abc import ABC,abstractmethod

class BankAccount(ABC):
    INTREST_RATE = 0.04

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'Initial balance is {balance}')

    @abstractmethod
    def deposit(self, Amount):
        if Amount < 0:
            raise ValueError('Amount should be greater than zero!!!')
        self.balance += Amount
        self.transactions.append(f'Amount deposited is {Amount}')

    def withdraw(self, Amount):
        if self.balance < Amount:
            raise ValueError('Insufficient Fund!!')
        self.balance -= Amount
        self.transactions.append(f'Amount withdrawn is {Amount}')

    def transfer(self, rev_account, Amount):
        self.withdraw(Amount)
        rev_account.deposit(Amount)
        self.transactions.append('Amount transferred from your account')
        rev_account.transactions.append('Amount received in your account')

    def roi(self):
        interest_amount = self.balance * self.__class__.INTREST_RATE
        self.deposit(interest_amount)
        self.transactions.append('Interest added to your account')

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print('*' * 30)
        print(f'Total current balance is {self.balance}')


# Objects
# c1 = BankAccount('Steve Jobs', 1000)
# c2 = BankAccount('Bill Gates', 2000)
# c3 = BankAccount('Tim Cook', 4000)


# class SavingAccount(BankAccount):
#     INTREST_RATE = 0.045

#     def __init__(self, name, balance, phone_number):
#         super().__init__(name, balance)
#         self.phone_number = phone_number
#     def withdraw(self, Amount):
#         if Amount<100:
#             raise ValueError('You withdraw minimum from 100 Rs')
#         super().withdraw(Amount)

# c4 = SavingAccount('Rolex', 4000, 9874561233)
# print(c4.__dict__)


# class SalaryAccount(SavingAccount):
#     INTREST_RATE = 0.045
#     def __init__(self, name, balance, phone_number,company_name):
#         super().__init__(name, balance,phone_number)
#         self.company_name = company_name

# c5 = SalaryAccount('Alex Star',50000,987615233,'TCS')
# c5.withdraw(500)
# c5.deposit(50)
# print(c5.__dict__)
