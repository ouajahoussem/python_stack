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
        
        return self.balance


    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:


    def __init__(self, name):
        self.name = name
        self.account = {
            "firstAccount": BankAccount(.05,2000),
            "secondAccount": BankAccount(.02, 5000)
        }


    def display_user_balance(self):
        print(f"User: {self.name}, firstAccount balance: {self.account["firstAccount"].display_account_info()}")
        print(f"User: {self.name}, secondAccount balance: {self.account["secondAccount"].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


Houssem = User("Houssem")
Houssem.account['firstAccount'].deposit(200)
Houssem.account['secondAccount'].withdraw(500)
Houssem.display_user_balance()

