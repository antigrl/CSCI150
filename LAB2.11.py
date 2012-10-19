numbers = [10,4,33,1,5,20]

def median():
	sorts = sorted(numbers)
	length = len(sorts)
	if not length % 2:
		return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
	return sorts[length / 2]

print median()