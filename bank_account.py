"""
This piece of code will simulate a bank account that can do the following:
accept deposits; allow withdrawals; show balance; show details of account.
"""

print # for tab
from termcolor import colored as clrd
from random import randint as rndm

class BankAcount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    # Display account:
    def __repr__(self):
        return "Account holder: %s \nBalance: $%.2f" % (
        self.name, self.balance)

    # Show balance to user:
    def show_balance(self):
        print "Balance: $%.2f\n" % (self.balance)

    # Deposit money:
    def deposit(self, amount):
        if amount <= 0:
            print "Cannot deposit that ammount."
            return
        else:
            print "Deposit amount:", clrd("+ $%.2f", 'green') % (amount)
            self.balance += amount
            self.show_balance()

    # Withdraw money:
    def withdraw(self, amount):
        if amount > self.balance:
            print "Insufficient funds to withdraw."
        else:
            print "Withdrawing amount:", clrd("- $%.2f", 'red') % (amount)
            self.balance -= amount
            self.show_balance()


my_account = BankAcount("Denis Matei")
#print my_account
#my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1001)
#print my_account
my_account.deposit(582)
my_account.withdraw(24)
my_account.deposit(582)
my_account.withdraw(111)
my_account.deposit(24)
my_account.withdraw(1)
my_account.deposit(3)
my_account.withdraw(7)
my_account.deposit(24)
my_account.withdraw(102)
my_account.deposit(20111235)
my_account.withdraw(25)
my_account.deposit(83595)
my_account.withdraw(49429)
my_account.deposit(123)
my_account.withdraw(1)
my_account.deposit(2)
my_account.withdraw(33)
my_account.deposit(555)
my_account.withdraw(1127)

# while True:
#     my_account.deposit(rndm(1,9999))
#     my_account.withdraw(rndm(1,999))