#!/usr/bin/env python3
# Parser Class

import urllib.request
from bs4 import BeautifulSoup
import sqlite3

class Parser:
    url = 'http://www.faz.net/rss/aktuell/'
    req = urllib.request.urlopen(url)
    data = req.read()
    xml = BeautifulSoup(data, features="xml")
    articles = []
    def __init__(self):
        pass

    def parseFAZ(self):
        for item in self.xml.findAll('item'):
            infoItem = {}
            infoItem['title'] = item.find('title').__str__()
            try:
                infoItem['date'] = item.find('pubDate')
            except Exception as e:
                infoItem['date'] = 'nA'
            infoItem['link'] = item.find('link')
            self.articles.append(infoItem)
        return self.articles



# f = open('news.json', 'wb')
# pickle.dump(articles, f)
# f.close()
# print('\n1')
