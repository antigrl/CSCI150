namefile = file('people.txt')
name = ''
for line in namefile:
	rightSpace = line.rindex(' ')
	year = int(line[rightSpace+1:])
	if name == '' or year < earlyYear:
		earlyYear = year
		name = line[:rightSpace]
	print name