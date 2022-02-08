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
    def __init__(self, first_name, last_name, email,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = dict([])

    def addNewAccount(self,accountName):
        self.accounts[accountName] = BankAccount(.05, 0)

    def addNewAccountWithAmmount(self,accountName, ammount):
            self.accounts[accountName] = BankAccount(.05, ammount)

    def addNewAccountWithInterestAndAmount(self,accountName,intrest_rate, amount):
            self.accounts[accountName] = BankAccount(intrest_rate, amount)


    def make_deposit(self, amount, accountName):
            self.accounts[accountName].make_deposit(amount)


    def make_withdraw(self, amount, accountName):
        self.accounts[accountName].make_withdraw(amount)

user1 = User("Kevin", "Centeno", "winner@gmail.com")
user2 = User('Andrew', "Centneo", "winners@gmail.com")

user1.addNewAccountWithAmmount("Savings", 100)
user1.addNewAccountWithAmmount("Checkings" ,500)
user1.addNewAccountWithInterestAndAmount("Retirement",0.07,1000)

user2.addNewAccountWithAmmount("Savings", 1100)
user2.addNewAccountWithAmmount("Checkings" ,2500)
user2.addNewAccountWithInterestAndAmount("Retirement",0.07,121000)

user1.make_withdraw(1000,"Savings")


# class User:
#     def __init__(self, first_name, email):
#         self.first_name = first_name
#         self.email = email
#         self.balance1 = BankAccount()
#         self.balance2 = BankAccount()
#     def make_deposit(self, amount, bank):
#         if bank == 1:
#             self.balance1.make_deposit(amount)
#         if bank == 2:
#             self.balance2.make_deposit(amount)
#         return self
#     def make_withdraw(self, amount, bank):
#         if bank == 1:
#             self.balance1.make_withdraw(amount)
#         if bank == 2:
#             self.balance2.make_withdraw(amount)
#         return self

# user1 = User("Kevin Centeno", "winner@gmail.com")
# user2 = User('Andrew Centneo', "winners@gmail.com")
# user1.make_deposit(100,1)
# user1.make_deposit(500,2)
# user1.make_withdraw(500,1).make_deposit(700,1)
# user1.balance1.display_account_info()
# user1.balance2.display_account_info()