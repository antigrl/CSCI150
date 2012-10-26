# return name + ' is ' + str(inches/12) + ' feet and ' + str(inches % 12) + ' inches'

def heightString(name, inches):
	return '%s is %f feet tall' %(name, inches/12.0)

def interestEarned(balance, rate):
	return 'you earned %.2f dollars in interest' %(balance * rate) # State how many points after decimal



print heightString('Kevin', 74)
print interestEarned(4324.32, 0.06)