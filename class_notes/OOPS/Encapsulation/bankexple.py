class BankAccount:
    INTREST_RATE = 0.04

    def __init__(self, name, balance, Account_num):
        self.name = name
        self.__balance = balance
        self.Account_num = Account_num
    
    def get_balance(self):
        acc_num = input('Enter your account number : ')
        if acc_num != self.Account_num:
            raise ValueError('Wrong Accoun Number!!!')
        return self.__balance
    
    def set_balance(self,Amount):
        acc_num = input('Enter your account number : ')
        if acc_num != self.Account_num:
            raise ValueError('Wrong Accoun Number!!!')
        self.__balance+=Amount
    balance = property(get_balance, set_balance)

c1 = BankAccount('Steve Jobs', 1000,"SBI123")
c2 = BankAccount('Bill Gates', 2000,"SBI456")
c3 = BankAccount('Tim Cook', 4000,"SBI997")

# print(c1.set_balance(5000))
# print(c1.get_balance())
# print(c1.balance)
c1.balance = 500
print(c1.balance)