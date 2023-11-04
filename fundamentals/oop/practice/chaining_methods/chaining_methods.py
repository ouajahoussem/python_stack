class User:


    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_with_drawal(self,amount):
        self.account_balance -= amount
        return self
        

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")
        return self
        
    
    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

Houssem = User("Houssem")
Yasser = User("Yasser")
Malek =User("Malek")

Houssem.make_deposit(400).make_deposit(500).make_deposit(200).make_with_drawal(300).display_user_balance()
Yasser.make_deposit(1000).make_deposit(200).make_with_drawal(300).make_with_drawal(200).display_user_balance()
Malek.make_deposit(2000).make_with_drawal(500).make_with_drawal(200).make_with_drawal(50).display_user_balance()
Houssem.transfer_money(400,Malek)
