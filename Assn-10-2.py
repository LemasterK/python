fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
import string
string.punctuation
count = 0
d = dict()
l = list()
hour = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    h = words[5] 
    hour = h.split(':')
    hr = hour[0]
    d[hr] = d.get(hr,0) + 1
for key,val in d.items():
    l.append( (key,val) )
l.sort()
for key,val in l :
    print key,val