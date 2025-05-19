class Account:
    count = 0

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        Account.count += 1

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amt
            print(f"Withdrawn {amt}. New balance: {self.balance}")

    def deposit(self, amt):
        self.balance += amt
        print(f"Deposited {amt}. New balance: {self.balance}")

    def check(self):
        return self.balance


# Create one account
ac_name = input("Enter the name :- ")
ac_number = int(input("Enter the account number :- "))
ac_balance = int(input("Enter the initial balance :- "))
account = Account(ac_name, ac_number, ac_balance)

# Menu-driven loop
while True:
    print("\n1. Check Balance \n2. Deposit Balance \n3. Withdraw Balance \n4. Exit \n5.Create New Account")
    choice = int(input("Enter your choice :- "))

    if choice == 1:
        bal = account.check()
        print("Account Balance :-", bal)
    elif choice == 2:
        amount = int(input("Enter the amount to be deposited :- "))
        account.deposit(amount)
    elif choice == 3:
        amount = int(input("Enter the amount to be withdrawn :- "))
        account.withdraw(amount)
    elif choice == 4:
        break
    elif choice == 5:
        ac_name = input("Enter the name :- ")
        ac_number = int(input("Enter the account number :- "))
        ac_balance = int(input("Enter the initial balance :- "))
        account = Account(ac_name, ac_number, ac_balance)
    else:
        print("Wrong Input")

print("The number of accounts created :-", Account.count)
