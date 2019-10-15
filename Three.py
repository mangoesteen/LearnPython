#Classes and Objects Example: 
#bank_account.py
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def withdraw(self,amount):
        self.balance -= amount
        return print(self.balance)

    def deposit(self,amount):
        self.balance += amount
        return print(self.balance)

a = BankAccount()
b = BankAccount()
a.deposit(100)
b.deposit(50)
b.withdraw(10)
a.withdraw(10)


# handling_exception.py #error
try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero")

#raising_error.py
try:
    a = int(input("Enter a negative integer: "))
    if a >= 0:
        raise ValueError("That is not a negative number!")
except ValueError as ve:
    print(ve)

#try…finally
try:
    f = open("test.txt", encoding='utf-8')
    # perform file operations
finally:
    f.close()


