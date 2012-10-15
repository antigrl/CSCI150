cheerlead = raw_input('Give me something to cheer for: ')

vowels = ['a','e','i','o','r','f','h','l','m','n','s','x']

def cheer(string):
	letters = list(string)

	for letter in letters:

		if vowels.count(letter.lower()) == 1:
			print 'Gimmie an ' + letter.capitalize()
		else:
			print 'Gimmie a ' + letter.capitalize()

	print 'What\'s that spell? ' + string

cheer(cheerlead)