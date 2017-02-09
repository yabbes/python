#!/usr/bin/env python3
# This is going to be the Financeer main program filter
from db import BankDatabase

class Financeer:
    def __init__(self, addedAmount):
        self.b = BankDatabase()
        self.userInput = ''
        self.accountBalance = self.b.getAccountBalance()
        self.temp = addedAmount
        self.newAccountBalance = self.b.getAccountBalance() + self.temp
        self.accountName = self.b.getAccountName()
        self.transactionCount = self.b.getNumberOfTransactions()
    def mainLoop(self):
        self.userInput = input()
        if self.userInput.startswith('.help'):
            self.helpFunctions()
        if self.userInput.startswith('.name'):
            self.name()
        if self.userInput.startswith('.temp'):
            self.temporary()
        if self.userInput.startswith('.balance'):
            self.balance()
        if self.userInput.startswith('.count'):
            self.count()
        if self.userInput.startswith('.add'):
            self.add()
        if self.userInput.startswith('.quit'):
            self.quit()


    def helpFunctions(self):
        print('Financeer kennt folgende Funktionen: \n'
        '.balance \t show account balance\n'
        '.temp \t\t show _temporary_ money\n'
        '.name \t\t show names of connected bank accounts\n'
        '.count \t\t show transaction count for bank accounts\n'
        '.add \t\t add money to _temporary money_\n'
        '.quit \t\t quit Financeer(r) \n')
    def name(self):
        print('Currently analysing account: {0}\n'.format(self.accountName))
    def getNewAccountBalance(self):
        return self.newAccountBalance
    def add(self):
        amt_str = self.userInput.split(' ',1)[1]
        try:
            amt_int = int(amt_str)
            self.temp = self.temp + amt_int
            self.newAccountBalance = self.newAccountBalance + amt_int
            print('Now handling {0} of temporary monies'.format(self.getTemporary()))
            # return self.temp + self.newAccountBalance
        except ValueError:
            print('The second parameter of .add is supposed to be an int')
    def balance(self):
        print('Current bank account balance {0}\n'.format(self.accountBalance))
    def getTemporary(self):
        return self.temp
    def temporary(self):
        print('Currently handling {0} € of temporary monies \n'.format(self.getTemporary()))
        print('if you were to save it to your bank account, this would make {0}'.format(self.getNewAccountBalance()))
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
