inp = raw_input("Enter Score between 0.0 and 1.0: ")
score=float(inp)
try:
	score=int(inp)
except:
	if score > 0:
		score = float(inp)
	else :
		print "not a number"
if score > 1:
    print "not within range specified!"
else:
    if score >= .9:
        grade = str('A')
    elif score >= .8:
        grade = str('B')
    elif score >= .7:
        grade = str('C')
    elif score >= .6:
        grade = str('D')
    else:
        grade = str('F')
    print grade   