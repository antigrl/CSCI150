from cs1graphics import *

numLevels = 4
unitSize = 12
screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)

for level in range(numLevels):
	width = (1+level)*unitSize
	block = Rectangle(width, unitSize)
	centerX = (numLevels-level/2.0)*unitSize
	centerY = (1+level)*unitSize
	block.move(centerX, centerY)
	block.setFillColor('Gray')
	paper.add(block)