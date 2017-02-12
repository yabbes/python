#!/usr/bin/env python3
# SQLITE3 DATABASE CLASS for my news parser
import sqlite3 as lite
import sys


class NewsDB:
    con = None

    def __init__(self):
        try:
            self.con = lite.connect('news.db')
            self.cur = self.con.cursor()
        except lite.Error as e:
            print(e)
            sys.exit(1)

    def closeConnection(self):
        self.con.close()
