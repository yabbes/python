#!/usr/bin/env python3
# This is going to be the Financeer main program filter
from db import BankDatabase

class Financeer:
    def __init__(self, addedAmount):
        self.b = BankDatabase()
        self.accountBalance = self.b.getAccountBalance()
        self.newAccountBalance = self.b.getAccountBalance() + addedAmount
        self.accountName = self.b.getAccountName()
        self.transactionCount = self.b.getNumberOfTransactions()
    def mainLoop(self):
        print('Aktueller Kontostand: \t {0} \t aus: {1}'.format(self.accountBalance,
        self.accountName))
        exit(0)


if __name__ == '__main__':
    print('Willkommen zur Bankübersicht von Financeer \n')
    print('Hast Du gerade noch Geld auf der Täsch? \n')
    try:
        monies = int(input())
    except ValueError:
        print('Bitte Geld als ganze Zahl eingeben\n'
        'Benutze >>0€<<\n')
        monies = 0
    fin = Financeer(monies)

    while True:
        fin.mainLoop()

    #print(fin.accountBalance)
    #fin.b.setAccountBalance(322)
