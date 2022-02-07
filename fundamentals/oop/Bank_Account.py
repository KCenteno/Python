class BackAccount:
    def __init__(self, intrest_rate=10, balance=0):
        self.intrest_rate = intrest_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        # print(f'Deposit:{self.intrest_rate}, Balance:{self.balance}')
        return self
    def make_withdraw(self, amount):
        amount -= self.balance
        # print(f'Withdraw:{self.intrest_rate}, Balance:{self.balance}')
        return self
    def display_account_info(self):
        # print(f'Balance:{self.balance}')
        return self
    def yield_intrest(self):
        y = 0
        if(self.balance > 0):
            y = self.balance * self.intrest_rate
            self.balance += y
        print(f'Balance:{self.balance}')
        return self

acct1 = BackAccount(.03, 0)
acct2 = BackAccount(.08, 200)

acct1.make_deposit(200).make_deposit(400).make_deposit(600).make_withdraw(400).yield_intrest()
acct2.make_deposit(1000).make_deposit(1000).make_withdraw(200).make_withdraw(100).make_withdraw(300).make_withdraw(200).yield_intrest()