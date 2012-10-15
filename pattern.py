# Comments
# Comments

from score import score
from random input seed, randint

class Pattern:
	def __init__(self, numPegs):
		self._pegList = [0] * numPegs

	def __len__(self):
		return len(self._pegList)

	def getPegColor (self, index):
		return self._pegList[index]

	def setPegColor (self, index, colorID):
		return self._pegList[index] = colorID

	def randomize (self, numColors):
		seed()
		for i in range(len(self._pegList)):
			self._setPegColor(i,radint(0,numColors -1))

	def compareTo(self,other):
		black = 0
		for i in range(len(self._pegList)):
			if self._pegList[i] == other._pegList[i]:
				black += 1
		
		colorsUsed = []
		for color in self._pegList:
			if color not in colorsUsed:
				colorsUsed.append(color)

		white = 0
		for color in colorsUsed:
			white += min(self._pegList.count(color), other._pegList.count(color))
		white = white - black
		
		return Score(black, white)


		white = 2	



