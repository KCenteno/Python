class BankAccount:
    def __init__(self, intrest_rate=.05, balance=100):
        self.intrest_rate = intrest_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        print(f'Balance:{self.balance}')
        return self
    def make_withdraw(self, amount):
        self.balance -= amount
        print(f'Balance:{self.balance}')
        return self
    def display_account_info(self):
        print(f'Balance:{self.balance}')
        return self
    def yield_intrest(self):
        y = 0
        if(self.balance > 0):
            y = self.balance * self.intrest_rate
            self.balance += y
        print(f'Balance:{self.balance}')
        return self


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.balance = BankAccount()


user1 = User("Kevin", "Centeno", "winner@gmail.com")
user2 = User('Andrew', "Centneo", "winners@gmail.com")
user1.balance.make_deposit(100).yield_intrest().display_account_info()
user2.balance.make_withdraw(500).make_deposit(500).yield_intrest().display_account_info()