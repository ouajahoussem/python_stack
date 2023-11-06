class BankAccount:
    accounts=[]
    def __init__(self,  int_rate, balance): 
        self.int_rate= int_rate
        self.balance= balance
        BankAccount.accounts.append(self)

        
        
    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self



    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

firstAccount= BankAccount(.05,2000)
secondAccount= BankAccount(.02, 5000)

firstAccount.deposit(50).deposit(100).deposit(20).withdraw(200).yield_interest().display_account_info()
secondAccount.deposit(100).deposit(300).withdraw(20).withdraw(200).withdraw(600).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all_accounts()
