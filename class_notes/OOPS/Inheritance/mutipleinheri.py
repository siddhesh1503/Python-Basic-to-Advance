########## Multiple Inheritance ############

class Object_data_collection:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'Initial balance is {balance}')


class Transactions:
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Amount should be greater than zero!!!')
        self.balance += amount
        self.transactions.append(f'Amount deposited is {amount}')

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Amount must be positive!')
        if self.balance < amount:
            raise ValueError('Insufficient Fund!!')
        self.balance -= amount
        self.transactions.append(f'Amount withdrawn is {amount}')

    def transfer(self, rev_account, amount):
        self.withdraw(amount)
        rev_account.deposit(amount)
        self.transactions.append('Amount transferred from your account')
        rev_account.transactions.append('Amount received in your account')


class Other_transactions:
    def roi(self):
        interest_amount = self.balance * self.__class__.INTEREST_RATE
        self.deposit(interest_amount)
        self.transactions.append('Interest added to your account')

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print('*' * 30)
        print(f'Total current balance is {self.balance}')


class Account(Object_data_collection, Transactions, Other_transactions):
    INTEREST_RATE = 0.045


c5 = Account('yash', 5000)
c5.withdraw(500)
c5.deposit(1000)
c5.roi()
c5.statement()
print(c5.__dict__)