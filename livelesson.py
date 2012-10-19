def demo():
	data = raw_input('Enter "y" or "n": ').strip()
	if data[0].lower() == 'y':
		print 'You typed "y"'
	elif data[0] == 'n':
		print 'You typed "n"'
	elif data == 'gooj':
		print 'You got out of jail free.'
	else:
		print 'You entered invalid key.'

def loopLesson():
	value = int(raw_input("Enter#: "))
	counter = int(value ** 0.5) # sq root

	while counter > 1: # stop at 2
		if value % counter == 0:
			print value, "is composite"
			break
		counter -= 1
	else:
		print value, "is prime"

loopLesson()