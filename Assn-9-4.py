fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
d = dict()
for line in fh :
    if not line.startswith('From ') : continue
    words = line.split()
    w = words[1]
    d[w] = d.get(w,0) + 1
largest = None
for key in d :
    if largest is None or d[key] > largest :
        largest = d[key]
        eml = key
# print eml, d.get(0,largest)
print eml, largest