#!/usr/bin/env python3
# start file for my rss parser
from newsDB import NewsDB
from parser import Parser

def main():
    n = NewsDB()
    n.cur.execute('Select SQLITE_VERSION()')
    data = n.cur.fetchone()

    print(data)
    p = Parser()
    articles = p.parseFAZ()
    print(articles)


if __name__ == '__main__':
    main()
