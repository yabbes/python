#!/usr/bin/env python3
# This is going to be the Financeer main program filter
from db import BankDatabase

class Financeer:
    def __init__(self, addedAmount):
        self.b = BankDatabase()
        self.accountBalance = self.b.getAccountBalance() + addedAmount
        self.accountName = self.b.getAccountName()
        self.transactionCount = self.b.getNumberOfTransactions()

if __name__ == '__main__':
    fin = Financeer(100)
    print(fin.accountBalance)
    #fin.b.setAccountBalance(322)
