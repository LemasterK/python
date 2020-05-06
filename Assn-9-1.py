fname = "words.txt"
fh = open(fname)
d = dict()
for line in fh :
    w = line.split()
    for word in w :
        d[word] = d.get(word,0) + 1
# if 'the' in d :
print d.get('hogwarts',0)
    