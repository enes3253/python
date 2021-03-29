class BankAccount:
	def _init_(self, int_rate = 0.01, balance = 0):
            self.int_rate = int_rate
            self.balance = balance
	def deposit(self, amount):
            self.balance += amount
            return self
	def withdraw(self, amount):
            if (self.balance >= amount):
                self.balance -= amount
            else:
                print('Insufficient funds: Charging a $5 fee')
                self.balance -= 5
            return self
	def display_account_info(self):
            print("Balance:$ {}".format(self.balance))
            return self
	def yield_interest(self):
            if (self.balance > 0):
                self.balance += self.int_rate * self.balance 
            return self

bankAccount = BankAccount(0.01, 30)
bankAccount2 = BankAccount(0.02, 40)

bankAccount.deposit(3).deposit(100).yield_interest().display_account_info()
bankAccount2.deposit(3).deposit(100).withdraw(2).withdraw(15).withdraw(3).withdraw(60).yield_interest().display_account_info()