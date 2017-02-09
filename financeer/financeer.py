#!/usr/bin/env python3
# This is going to be the Financeer main program filter
from db import BankDatabase

class Financeer:
    def __init__(self, addedAmount):
        self.b = BankDatabase()
        self.accountBalance = self.b.getAccountBalance()
        self.temp = addedAmount
        self.newAccountBalance = self.b.getAccountBalance() + addedAmount
        self.accountName = self.b.getAccountName()
        self.transactionCount = self.b.getNumberOfTransactions()
    def mainLoop(self):
        userInput = input()
        if userInput.startswith('.help'):
            self.helpFunctions()
        if userInput.startswith('.name'):
            self.name()
        if userInput.startswith('.temp'):
            self.temporary()
        if userInput.startswith('.balance'):
            self.balance()
        if userInput.startswith('.count'):
            self.count()
        if userInput.startswith('.quit'):
            self.quit()


    def helpFunctions(self):
        print('Financeer kennt folgende Funktionen: \n'
        '.balance \t show account balance\n'
        '.temp \t\t show _temporary_ money\n'
        '.name \t\t show names of connected bank accounts\n'
        '.count \t\t show transaction count for bank accounts\n'
        '.quit \t\t quit Financeer(r) \n')
    def name(self):
        print('Currently analysing account: {0}\n'.format(self.accountName))
    def balance(self):
        print('Current bank account balance {0}\n'.format(self.accountBalance))
    def temporary(self):
        print('Currently handling {0} € of temporary monies \n'.format(self.temp))
        print('if you were to save it to your bank account, this would make {0}'.format(self.newAccountBalance))
    def count(self):
        print('Currently counting {0} transactions on this bank account \n'.format(self.transactionCount))
    def quit(self):
        print('Ciao\n')
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
    print('Aktueller Kontostand: \t {0} \t aus: {1}'.format(fin.accountBalance,
    fin.accountName))
    while True:
        fin.mainLoop()

    #print(fin.accountBalance)
    #fin.b.setAccountBalance(322)
