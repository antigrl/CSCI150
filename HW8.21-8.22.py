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
		words = list()
		symbols = [",", ".", "?", "!", "..."]
		for entry in f:
			for word in entry.strip('\n',symbols).split():
				words.append(word)

		invalidWords = list()
		for word in words:
			if word not in self:
				invalidWords.append(word)
		return invalidWords



if __name__ == '__main__':
	# unit test
	vocab = Vocabulary()
	print vocab._vocab
	
	print 'Python' in vocab
	print 'arthur' in vocab

	print vocab.check('en.test.txt')
