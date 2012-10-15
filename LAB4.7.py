from cs1graphics import *

numLevels = int(raw_input('Enter number of levels: '))
unitSize = int(raw_input('Enter heigh of pyramid: '))
screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)
centerX = screenSize / 2.0

for level in range(numLevels):
	centerY = (level + 1) * unitSize
	leftmostX = centerX - unitSize * level / 2.0
	for blockCount in range(level + 1):
		block = Square(unitSize)
		block.move(leftmostX + unitSize * blockCount, centerY)
		block.setFillColor('gray')
		paper.add(block)

