fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
import string
string.punctuation
count = 0
d = dict()
hour = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    h = words[5] 
    hour = h.split(':')
    hr = hour[0]
    # print hour[0]
    d[hr] = d.get(hr,0) + 1
# d = sorted
print d
smallest = None
#for key in d :
#    if smallest is None or d[key] < smallest :
#        smallest = d[key]