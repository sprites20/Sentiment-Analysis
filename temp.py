import re
import time

def inner_regex(s):
    return re.sub(r'<[^>]*>', '', s)

def inner_regex_compiled(s,r):
    return r.sub('', s)

def inner_substr(s):
    s_ind = s.find('>') + 1
    e_ind = s.find('<', s_ind)
    return s[s_ind:e_ind]


s = '<stuff to remove> get this stuff <stuff to remove>'

s3 = inner_substr(s)
print(s3)