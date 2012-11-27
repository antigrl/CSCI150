class Vocabulary():
	def __init__(self):
		f = open('en.txt', 'r') 														# open in read mode
		self._vocab = list()
		for entry in f:
			self._vocab.append(entry.rstrip('\n'))						# remove trailing newline

	def __contains__(self, value):
		for entry in self._vocab:
			if entry[0].isupper():
				if value == entry:
					return True
			else:
				if value.lower() == entry:
					return True
		return False

	def check(self, file):
		f = open(file)
		o = open('new.txt','w')															# Correct spellings get written to this file
		lineNum = 0
		for line in f:
			lineNum += 1
			for word in line.split():													# Find punctuation and remove it from the word
				if word.find(',') > -1:
					word = word.strip(',')
					punct = ','
				elif word.find('.') > -1:
					word = word.strip('.')
					punct = '.'
				elif word.find('!') > -1:
					word = word.strip('!')
					punct = '!'
				elif word.find('?') > -1:
					word = word.strip('?')
					punct = '?'

				if word not in self:
					print word, lineNum
					prompt = raw_input('Would you like to ignore(I) or replace(R) spelling mistake? ')
					if prompt is 'I':
						o.write(word + ' ')
					if prompt is 'R':															# User can replace the incorrect spelling with a suggestion or use their own
						suggestions = self.getSuggestions(word)								
						if len(suggestions) == 0:
							easyReplace = -1
						else:
							for i in range(len(suggestions)):
								print i , ': ', suggestions
							easyReplace = raw_input('Enter the index to replace the word with the suggestion: ')
						if easyReplace > -1:
							o.write(suggestions[int(easyReplace)] + ' ')
						else:
							newWord = raw_input('Replace the word: ')
							o.write(newWord + ' ')
				else:
					o.write(word + ' ')

	def getSuggestions(self, misspelledWord):
		"""Check the word that's been passed against every word in Vocabulary and if there's only one letter difference, then return it as a suggestion.
		"""
		suggestions = []
		for dictWord in self._vocab:
			dictLetters = list(dictWord)
			misspelledLetters = list(misspelledWord)
			count = 0
			if len(dictWord) == len(misspelledWord):
				for i in range(len(dictWord)):
					if dictLetters[i] != misspelledLetters[i]:
						count += 1
				if count < 2:
					suggestions.append(dictWord)
		return suggestions


if __name__ == '__main__':
	# unit test
	vocab = Vocabulary()

	vocab.check('1.txt')																		# I tested the spellchecker by generating a file that randomly replaced a letter in each word of the en.txt file











