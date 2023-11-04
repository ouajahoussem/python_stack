class User:


    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_with_drawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")
    
    def transfer_money(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


Houssem = User("Houssem")
Yasser = User("Yasser")
Malek =User("Malek")

Houssem.make_deposit(400)
Houssem.make_deposit(500)
Houssem.make_deposit(200)
Houssem.make_with_drawal(300)
Houssem.display_user_balance()

Yasser.make_deposit(1000)
Yasser.make_deposit(200)
Yasser.make_with_drawal(300)
Yasser.make_with_drawal(200)
Yasser.display_user_balance()

Malek.make_deposit(2000)
Malek.make_with_drawal(500)
Malek.make_with_drawal(200)
Malek.make_with_drawal(50)
Malek.display_user_balance()

Houssem.transfer_money(400,Malek)


