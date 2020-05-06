count = 0
sum = 0
avg = 0
def avg():
    avg = sum / count
while True:
    inp = raw_input("Enter a number : ")
    if inp == 'done' :
        break
    try:
        num=int(inp)
    except:
        print "Invalid input"
        continue 
    sum = sum + num
    count = count +1
avg = sum / count
print sum, count, avg 
    