class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def displayBalance(self):
        print(f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: ${self.balance}\n")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        self.calculateInterest()

    def calculateInterest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            available_funds = self.balance + self.overdraft_limit
            if amount <= available_funds:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Withdrawal amount exceeds available funds.")
        else:
            print("Invalid withdrawal amount.")



savings_account = SavingsAccount("SA123", "John Doe", 1000, 5)
current_account = CurrentAccount("CA456", "Jane Smith", 2000, 500)

savings_account.deposit(200)
savings_account.withdraw(100)
savings_account.displayBalance()

current_account.withdraw(2500)
current_account.displayBalance()