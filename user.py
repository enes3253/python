class User:
    def __init__(self , name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,ammount):
        self.account_balance += ammount
        return self

    def print_balance(self):
        print(self.account_balance)
        return self

    def make_withdrawl(self,ammount):
        self.account_balance -= ammount
        return self

    def make_transfer(self,ammount,user):
        self.account_balance -= ammount
        user.account_balance += ammount
        return self

user1 = User ("User 1", "user@gmail.com")
user2 = User ("User 2", "user2@gmail.com")
user3 = User ("User 3", "user3@gmail.com")

user1.make_deposit(1).make_deposit(4).make_deposit(7).make_withdrawl(7).print_balance()

user2.make_deposit(10).make_deposit(5).make_withdrawl(8).make_withdrawl(7).print_balance()

user3.make_deposit(50).make_withdrawl(10).make_withdrawl(20).make_withdrawl(5).print_balance()

user1.make_transfer(10, user2).print_balance()

user2.make_transfer(20, user3).print_balance()

user3.make_transfer(30, user1).print_balance()
