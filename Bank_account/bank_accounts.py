class BalanceException(Exception):
    pass


class BakAccount:
    def __init__(self, initialAmmount, acctName):
        self.balance = initialAmmount
        self.name = acctName

        # f before the "" means its an f string, used if we intent to have names and decimal values in the print statement
        # \n - called a line break,is for next line
        # we specify variables with curly braces inside the string
        # :.2f - tells a 2 decimal place
        print(f"\n Account for {self.name} created \n with an ammount of ${self.balance:.2f} \n")

    def getBalance(self):
        print(f"\n Account for {self.name} has \n a balance of ${self.balance:.2f} \n")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\n Account for {self.name} \n deposit ammount = ${amount:.2f} \n new balance = ${self.balance:.2f} \n")
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account {self.name} only has a balance of ${self.balance:.2f}"
                )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n Withdraw of ${amount} complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print('\n ******************\n Beninging Transfer ... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer complete! ✅ \n***************")
        except BalanceException as error:
            print(f"\n Transfer interrupted.  ❌ {error}")

# Inheritance
class interestRewardsAcc(BakAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\n Deposit complete")
        self.getBalance()

class savingsAcc(interestRewardsAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")


