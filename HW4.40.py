from cs1graphics import *

paper = Canvas(400,400)
height = 8
width = 8
size = 50

for row in range(0,8,1):
	for column in range(0,8,1):
		square = Square(50)
		square.move(25+50 * column,25+50 * row)
		paper.add(square)

		# If the row plus the column is an odd number then it's black
		if (row + column) % 2 == 0:
			square.setFillColor('red')
		else:
			square.setFillColor('black')
			if row < 3:
				checkers = Circle(20)
				checkers.setFillColor('white')
				checkers.setBorderColor('white')
				checkers.move(25+50 * column,25+50 * row)
				paper.add(checkers)
			if row > 4:
				checkers = Circle(20)
				checkers.setFillColor('red')
				checkers.setBorderColor('red')
				checkers.move(25+50 * column,25+50 * row)
				paper.add(checkers)



