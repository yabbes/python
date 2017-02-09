#!/usr/bin/env python3
# This file is supposed to start Financeer
from financeer import Financeer

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
