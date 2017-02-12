#!/usr/bin/env python3
# Duden word lookup and spelling checker
# coding=utf-8

import urllib.request
from bs4 import BeautifulSoup
import sys


def main(word):
    url = 'http://www.duden.de/suchen/dudenonline/'+word
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
    req = urllib.request.Request(url, headers=headers)
    req_open = urllib.request.urlopen(req)
    data = req_open.read()
    parse(data)


def parse(data):
    soup = BeautifulSoup(data, 'lxml')
    firstResult_filter = {"id": "block-duden-tiles-0"}
    firstResult = soup.find('section', firstResult_filter)
    # for later tries, getting description text as well maybe
    # sections = firstResult.findAll('section', {"class":"wide"})
    # for item in sections:
    #     print('{0}'.format(item.next_sibling()))

    firstResult_headers = firstResult.findAll('a', {"class": "hidden-link"})

    for item in firstResult_headers:
        print('{0}'.format(item.text))

    # debugging purposes:
    # f = open("duden.html", 'w')
    # soup_str = str(firstResult_headers)
    # f.write(soup_str)
    # f.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        try:
            main(word)
        except Exception as e:
            # because duden.de does not handle httprequests for words
            # that don't exist, we can simply conclude the following
            # at least for our purposes it will be just fine
            print(
                  'This word either does not exist'
                  'or is not spelled correctly \n'
                  )
    else:
        print(
            "Please enter the word for lookup as parameter\n"
            "Correct syntax : ./duden.py ##word##\n")
