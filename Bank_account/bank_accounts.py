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
    