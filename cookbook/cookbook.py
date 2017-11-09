# Start of my little albeit very handy Python cookbook

# finding number of occurences in string via regex (re)
import re
def count_code(s):
    regex = re.compile('(co.e)')
    return len(regex.findall(s))

# normal way of counting occurences of substring sx in string s
s.count(sx)


# looping with indexes in python
# example to emulate C style loop with running index i
i = 0
while i < len(array):
    print(array[i])
    i += 1

# calculate the number of days between two dates
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print(delta.days)
