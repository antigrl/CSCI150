groceries = ['milk','cheese','bread','cereal']


position = 0

while position < len(groceries):
	label = str(1 + position) + '. '
	print label + groceries[position]
	position += 1
