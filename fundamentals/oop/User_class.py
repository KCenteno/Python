class User:
    def __init__(self, first_name, email, balance=5000):
        self.first_name = first_name
        self.email = email
        self.balance = balance
    def make_withdrawal(self, withdraw):
        self.balance -= withdraw
        # print(f'User:{self.first_name}, Balance:{self.balance}')
        return self
    def make_deposit(self, amount):
        self.balance += amount
        # print(f'User:{self.first_name}, Balance:{self.balance}')
        return self
    def check_balance(self):
        print(f'User:{self.first_name}, Balance:{self.balance}')
    def tranfer_money(self, user, amount):
        self.balance -= amount
        user.balance += amount
        print(f'User:{self.first_name}, New Balance:{self.balance}')
        print(f'User:{user.first_name}, New Balance:{user.balance}')
        return self
    def tostring(self):
        print(f'User:{self.first_name}, New Balance:{self.balance}, email:{self.email}')



user1 = User("Kevin Centeno", "winner@gmail.com")
user2 = User("Andrew Centeno", "winner@gmail.com")
user3 = User("Bianca Centeno", "winner@gmail.com")

user1.make_deposit(600).make_deposit(600).make_deposit(600).make_withdrawal(1600)
user2.make_deposit(300).make_deposit(300).make_withdrawal(1000).make_withdrawal(1000)
user3.make_deposit(1000).make_withdrawal(200).make_withdrawal(100).make_withdrawal(10000)

user1.check_balance()
user2.check_balance()
user3.check_balance()
user1.tranfer_money(user3, 10000)
user1.tostring()
user2.tostring()
user3.tostring()
