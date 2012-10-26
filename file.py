
try:
	myfriends = file('friends.txt', 'r')
except IOError:
	print 'Could not open the file friends.txt'


