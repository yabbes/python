#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    source = "http://www.gelbeseiten.de/zahnarzt/herne"
    # source = "http://www.gelbeseiten.de/arzt/herne"
    # next content results are on link + /s2++
    r = requests.get(source)
    soup = BeautifulSoup(r.content, "html.parser")

    results = soup.find_all("span", {"itemprop": "name"})
    i = 1

    for result in results:
# <span itemprop="name"> %s </span>
        print("%d : %s " % (i, result.text))
        i += 1

    j = 2
    for j in range (9):
        if j == 2:
            source = source + "/s%d" % j
        else:
            source = source[:-2]
            source = source + "s%d" % j
        
        r = requests.get(source)
        # print("%s" % source)
        soup = BeautifulSoup(r.content, "html.parser")
        results = soup.find_all("span", {"itemprop": "name"})
        
        for result in results:
            print("%d : %s " % (i, result.text))
            i  += 1
        j += 1     
if __name__ == '__main__':
    main()
