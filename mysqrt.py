
# Strategy for computing square roots:
# GUESS!
# to see if you were right, multiply the guess by itself

def mysqrt(x):
	guess = 1.0
	other = x / guess
	while guess != other:
		guess = (guess + other) / 2.0
		other = x / guess
	return guess

x = int(raw_input('Input a number: '))
print mysqrt(x)

