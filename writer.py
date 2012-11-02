number = file('numbers.txt', 'w') # create a new file for writing

for x in range(0,1000):
	number.write(str(x) + '\n')
	pause = raw_input('enter a string to continue: ')

source.close()

