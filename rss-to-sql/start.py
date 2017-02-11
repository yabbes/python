#!/usr/bin/env python3
# start file for my rss parser
from newsDB import NewsDB
from parser import Parser

def main():
    n = NewsDB()
    n.cur.execute('Select SQLITE_VERSION()')
    data = n.cur.fetchone()
    p = Parser()
    articles = p.parseFAZ()


    for item in articles:
        # print(type(item['title']))
        n.cur.execute('INSERT INTO News (title, link, date) VALUES(?,?,?)', ('test', 'test', 'date'))
    # being a good guy, closing the connection
    n.con.commit()
    n.closeConnection()




if __name__ == '__main__':
    main()
