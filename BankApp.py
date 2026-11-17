''' Create a class named BankAccount with the following requirements:
1. Create a parameterized constructor accepting account_holder and balance.
2. Create a method called deposit(amount) to add money to the balance.
3. Create a method called withdraw(amount) to deduct money from the balance.
4. Create a method called display_balance() to display the current balance.
5. Create an object with:
   - Account holder: Sameer
   - Initial balance: ₹10,000
6. Deposit ₹2,000 and withdraw ₹3,000. '''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print("Account Holder : "+self.account_holder)
        print("Balance is : ",self.balance)

B1 = BankAccount("Sameer",30000)
B1.display()
B1.deposit(20000)
B1.display()
B1.withdraw(10000)
B1.display()


        
