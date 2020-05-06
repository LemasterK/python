def computepay(h,r):
    return (rate * 40) + (rate * 1.5 * (hrs - 40))

inp = raw_input("Enter Rate: ")
rate=float(inp)

inp = raw_input("Enter Hours: ")
hrs=float(inp)

if hrs <= 40 :
    pay = rate * hrs
elif hrs > 40 :
    p = computepay(hrs,rate)
print p
