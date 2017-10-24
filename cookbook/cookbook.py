# Start of my little albeit very handy Python cookbook

# finding number of occurences in string via regex (re)
import re
def count_code(s):
    regex = re.compile('(co.e)')
    return len(regex.findall(s))

# normal way of counting occurences of substring sx in string s
s.count(sx)
