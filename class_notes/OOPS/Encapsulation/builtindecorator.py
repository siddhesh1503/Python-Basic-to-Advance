class BankAccount:
    INTREST_RATE = 0.04

    def __init__(self, name, balance, Account_num):
        self.name = name
        self.__balance = balance
        self.Account_num = Account_num

    @property
    def balance(self):
        acc_num = input('Enter your account number : ')
        if acc_num != self.Account_num:
            raise ValueError('Wrong Accoun Number!!!')
        return self.__balance
    
    @balance.setter
    def balance(self,Amount):
        acc_num = input('Enter your account number : ')
        if acc_num != self.Account_num:
            raise ValueError('Wrong Accoun Number!!!')
        self.__balance += Amount
  

c1 = BankAccount('Steve Jobs', 1000,"SBI123")
c2 = BankAccount('Bill Gates', 2000,"SBI456")
c3 = BankAccount('Tim Cook', 4000,"SBI997")

c1.balance = 500
print(c1.balance)