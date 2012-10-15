class Fraction:

	def __init__(self, numerator, denominator):
		if denominator < 0:
			numerator *= -1
			denominator *= -1
		self._num = numerator
		self._denom = denominator

	def __str__(self):
		numPrint = self._num
		denomPrint = self._denom
		if self._num == 0:
			return '0'
		else:
			return str(numPrint) + '/' + str(denomPrint)

	def __add__(self, other):
		return Fraction(self._num*other._denom + self._denom*other._num, self._denom*other._denom)
		