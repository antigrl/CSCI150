def anagrams(lexicon, word, prefix=''):
	solutions = []
	if len(word) > 1:
		for i in range(word):
			newPrefix = prefix + word[i]
			newWord = word[0:i] + word[i+1:]
			solutions.extend(anagrams(lexicon, newWord, newPrefix))
	else:
		candidate = prefix + word
		if candidate in lexicon:
			solutions.append(candidate)
	return solutions