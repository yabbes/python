#!/usr/bin/env python
# Sorry this is lazy Python2 code but it did serve its purpose

import kopano
import csv

k = kopano.Server(auth_user='username',auth_pass='password', server_socket='http://zarafaserver:236/zarafa')

with open('output.csv','w') as f:        
    w = csv.writer(f, delimiter=",")
    w.writerow(['', 'User', 'Folder','Permissions'])
    for u in k.users(): 
        print u.name
        for p in u.store.permissions():
            try:
                w.writerow(['Store Permissions for: ', str(u.name).encode('utf-8'), '', ''])
            except UnicodeEncodeError:
                print "unicode error"
            try:
                w.writerow(['', str(p.member.name).encode('utf-8'), 'userstore', p.rights])
            except UnicodeEncodeError:
                print "unicode error"

        for f in u.store.folders():
            for fp in f.permissions():
                try:
                    w.writerow (['Listing', str(u.name).encode('utf-8'), 'Folder: ' + str(f.path).encode('utf-8'), ':'])
                except UnicodeEncodeError:
                    "unicode error"
                try:
                     w.writerow (['', str(fp.member.name).encode('utf-8'), str(f.path).encode('utf-8'), fp.rights])
                except UnicodeEncodeError:
                    print "unicode error"

    

