class Vocabulary():
	def __init__(self):
		f = open('en.txt', 'r') 										# open in read mode
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
		o = open('new.txt','w')
		lineNum = 0
		for line in f:
			lineNum += 1
			for word in line.split():
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
					prompt = raw_input('Would you like to ignore(I) or replace(R) spelling mistake?')
					if prompt is 'i':
						o.write(word + ' ')
					if prompt is 'r':
						newWord = raw_input('Replace the word: ')
						o.write(newWord + ' ')
				else:
					o.write(word + ' ')

if __name__ == '__main__':
	# unit test
	vocab = Vocabulary()

	vocab.check('1.txt')