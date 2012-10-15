def print_verse(n):
	if n == 1:
		print str(n) + ' bottle of beer on the wall'
		print str(n) + ' bottle of beer'
	else:
		print str(n) + ' bottle of beer on the wall'
		print str(n) + ' bottles of beer'
	print 'take one down pass it around'
	if n == 2:
	print str(n-1) + ' bottles of beer on the wall'

for x in range(99,0,-1):
	print_verse(x)