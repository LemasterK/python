fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
total = 0
for line in fh:
    line.rstrip()
    lst=line.split()
    count = 0
    if len(lst) == 0 : continue
    print len(lst)
    while count < len(lst) :
        l = lst[count]
        print l
        if l not in words : words.append(l)
        # words.append(l)
        count=count + 1
words.sort()
print words