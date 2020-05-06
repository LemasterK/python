# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float(line[pos+1:])
    count = count + 1
    tot = tot + num
avg = float(tot / count)   
print "Average spam confidence:",avg
