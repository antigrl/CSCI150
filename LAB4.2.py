def dramatic(word):
	answer = ''
	for letter in word:
		answer += letter * 2
	return answer

print dramatic('argh')
