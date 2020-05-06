fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
count = 0
for line in fh:
    line.rstrip()
    lst=line.split()
    # words.append(line.split())
    words=words+lst
    count=count + 1
    print lst
    print count
    print line
words.sort()
print words