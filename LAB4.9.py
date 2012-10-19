n=4
star = '*'
for i in range(n):
	starGroup = star * (i + 1)
	rightAlign = starGroup.rjust(n)
	print rightAlign