#!/usr/bin/env python3
# this is going to be the database class
# I want to use a simple json file as my database
import json

class BankDatabase:
    def __init__(self):
        with open('main.json', "r") as data_file:
            self.data = json.load(data_file)
    def getAccountName(self):
        return self.data['AccountName']
    def getAccountBalance(self):
        return self.data['AccountBalance']
    def getNumberOfTransactions(self):
        return self.data['NumberOfTransactions']
    def writeToDb(self):
        with open("main.json", "w") as jsonFile:
            jsonFile.write(json.dumps(self.data))
    def setAccountBalance(self, amount):
        self.data['AccountBalance'] = amount
        self.writeToDb()
    def setAccountName(self, name):
        self.data['AccountName'] = name
        self.writeToDb()
    def setTransactionCount(self, count):
        self.data['NumberOfTransactions'] = count
        self.writeToDb()
