from bank_accounts import *

sayan = BakAccount(1000, "sayan")
kri = BakAccount(2000, "KB")

sayan.getBalance()
sayan.deposit(5000)

sayan.withdraw(10000)
sayan.withdraw(1000)

sayan.transfer(100000, kri)
sayan.transfer(100, kri)

pank = interestRewardsAcc(1000, "pank")
pank.deposit(100)
pank.getBalance()

pank.transfer(100,sayan)

blaz = savingsAcc(1000, "blaz")

blaz.getBalance()
blaz.deposit(100)
blaz.transfer(10000, kri)
blaz.transfer(1000, kri)