u = int(raw_input('Enter first number: '))
v = int(raw_input('Enter second number: '))

guess = min(u,v)
while u % guess > 0 or v % guess > 0:
	guess -= 1

print 'The gcd is', guess