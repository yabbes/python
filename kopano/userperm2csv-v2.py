#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kopano
import csv

k = kopano.Server(auth_user='user',auth_pass='pass', server_socket='http://zarafaserver.de:236/zarafa')

with open('output.csv','w') as f:        
    w = csv.writer(f, delimiter=",")
    w.writerow(['Beschreibung', 'Besitzer', 'Rechteinhaber','Berechtigungen', 'Ordnername'])
    for u in k.users(): 
        print u.name
        for p in u.store.permissions():
            try:
                w.writerow(['Userstore von Benutzer: ', str(u.name), '', '', ''])
            except UnicodeEncodeError:
                print "unicode error"
            try:
                w.writerow(['Berechtigung', str(u.name), str(p.member.name), p.rights, 'Userstore'])
            except UnicodeEncodeError:
                print "unicode error"

        for f in u.store.folders():
            for fp in f.permissions():
                try:
                    w.writerow (['Ordnerberechtigungen von Benutzer', str(u.name), '', '', str(f.path)])
                except UnicodeEncodeError:
                    print "unicode error"

                try:
                    w.writerow (['Berechtigung', str(u.name), str(fp.member.name), fp.rights, f.path])
                except UnicodeEncodeError:
                    print "unicode error"

    

