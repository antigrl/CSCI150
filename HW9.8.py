from cs1graphics import *
from math import cos, sin, pi

class RegularPolygon(Polygon):
	"""Define a specialized RegularPolygon class, such that all side lengths and angles are consistent.
	"""

	def __init__(self, position=Point(0,0), numOfSides=2, lengthOfSides=10):
		Polygon.__init__(self)                    # call the parent constructor
		self._numOfSides = numOfSides
		self._lengthOfSides = lengthOfSides

		self._angle = 2*pi/numOfSides;

		for i in range(numOfSides):
			self.addPoint(
				Point(
					position.getX()+lengthOfSides*cos(self._angle*i),
					position.getY()+lengthOfSides*sin(self._angle*i)))

if __name__ == '__main__':
	# unit test
	screen = Canvas()
	screen.add(RegularPolygon(Point(50,50),4,50))






