#!/usr/bin/env python3
# searching on google powered by python avoiding Google's API

import urllib.request
import urllib.parse


values = {'q':'python tutorials'}
data = urllib.parse.urlencode(values)
url = 'https://www.google.de/search?'+data
data = data.encode('utf-8')

headers={}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
