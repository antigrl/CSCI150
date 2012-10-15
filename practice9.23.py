from cs1graphics import *

numLevels = 8  								# number of levels
unitSize = 12  								# the height of one level
screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)
centerX = screenSize / 2.0					# same for all levels

# create levels from top to bottom
for level in range(numLevels):
	width = (level + 1) * unitSize
	block = Rectangle(width, unitSize)
	centerY = (level + 1) * unitSize
	block.move(centerX, centerY)
	block.setFillColor('gray')
	paper.add(block)