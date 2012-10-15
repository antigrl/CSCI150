def dramatic(original, n=2):
	answer = ''
	for letter in original:
		#same as answer + answer = original*2
		answer +=  letter*n
	return answer


print dramatic('argh', 2)