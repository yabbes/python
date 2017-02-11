#!/usr/bin/env python3
# Duden word lookup and spelling checker

import urllib.request
from bs4 import BeautifulSoup
import sys



def main(word):
    url = 'http://www.duden.de/suchen/dudenonline/'+word
    headers={}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
    req = urllib.request.Request(url, headers=headers)
    req_open = urllib.request.urlopen(req)
    data = req_open.read()
    parse(data)

def parse(data):
    soup = BeautifulSoup(data, 'lxml')

    firstResult_filter = {"id":"block-duden-tiles-0"}
    noResult_filter = {"id":"block-system-main"}

    firstResult = soup.find('section', firstResult_filter)
    firstResult_headers = firstResult.findAll('a', {"class":"hidden-link"})

    for item in firstResult_headers:
        print('{0}'.format(item.text))

    f = open("duden.html", 'w')
    soup_str = str(firstResult_headers)
    f.write(soup_str)
    f.close()

    # noResult = soup.find('section', noResult_filter)
    # print('{0}\n {1}\n'.format(firstResult_headers.text(), noResult))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        try:
            main(word)
        except Exception as e:
            print('This word either does not exist or is not spelled correctly\n'
            '{}'.format(e))
    else:
        print("Please enter the word for lookup as parameter\n"
        "Correct syntax : ./duden.py ##word##\n")
