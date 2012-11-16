from cs1graphics import *

class Star(Drawable):
	def __init__(self, numRays=5, outerRadius=10, innerRatio=.5, center=Point(50,50), bodyColor = 'green'):
		Drawable.__init__(self)			         # call the parent constructor
		top = Point(0, -outerRadius)	         # top point is directly above origin
		angle = 180.0 / numRays

		self._polygon = Polygon()
		for i in range(numRays):
			self._polygon.addPoint(top ^ (angle * (2 * i)))
			self._polygon.addPoint(innerRatio * top ^ (angle * (2 * i + 1)))    # outer point

		
		self._polygon.adjustReference(0, outerRadius)      # move reference from top point to center
		self._polygon.move(center.getX(), center.getY())   # re-center entire star
		self._polygon._innerRatio = innerRatio             # record as an attribute

	def setInnerRatio(self, newRatio):
		factor = newRatio / self._innerRatio
		self._polygon._innerRatio = newRatio
		for i in range(1, self.getNumberOfPoints(),2):                 # inner points only
		    self._polygon.setPoint(factor * self.getPoint(i), i)

	def setBorderWidth(self, BorderWidth):
		self._polygon.setBorderWidth(BorderWidth)

	def setBorderColor(self, BorderColor):
		self._polygon.setBorderColor(BorderColor)

	def setFillColor(self, FillColor):
		self._polygon.setFillColor(FillColor)

	def _draw(self):
		self._beginDraw()                         # required protocol
		self._polygon._draw()
		self._completeDraw()                      # required protocol

if __name__ == '__main__':
	# Unit test
	star = Star()
	screen = Canvas()
	screen.add(star)
	star.setFillColor('green')
	star.setBorderColor('red')
	star.setBorderWidth(3)

