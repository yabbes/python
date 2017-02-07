#!/bin/env python3
##hangman project

import urllib.request
import random
from bs4 import BeautifulSoup

##prerequisites; building the database, reading some Maupassant
source = 'http://maupassant.free.fr/textes/solitude.html'
open = urllib.request.urlopen(source)
open_str = open.read().decode('utf-8')
soup = BeautifulSoup(open_str, "html.parser")
results = soup.get_text()
words = str.split(results)
filtered_db = list(filter(lambda x: len(x) >= 3, words))
## Now I have my word database, return exactly one word that is at least 3
## chars long, this will be our hangmanWord
hangmanWord = str.upper(random.choice(filtered_db))
word_guessed = []
for w in hangmanWord:
    word_guessed.append("_")

def gameLoop():
    guessed = []
    while True:
        print("Please enter a character\n")
        userInput = str.upper(input())
        if userInput in guessed:
            print("you have already said this letter")
            continue
        else:
            guessed.append(userInput)
        if userInput in hangmanWord:
            print("BIEN, the letter is part of the word we are looking for")
            for index, letter in enumerate(hangmanWord):
                if letter == userInput:
                    word_guessed[index] = userInput
        else:
            print("Sorry, but this letter is not part of the word")
        print(word_guessed)
        if checkIfComplete() is True:
            print("Congratulations, you've found the word\n")
            break
        ##print("debug info {0}".format(hangmanWord))

def main():
    print("Welcome to Hangman à la Maupassant\n"
    "I found the word, now it's your turn to guess it\n"
    "Good Luck")
    print("The word you are looking for is {0} characters long".format(len(hangmanWord)))
    gameLoop()

def checkIfComplete():
    summe = 0
    for n in word_guessed:
        if n == "_":
            summe = +1
    if summe > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    main()
