# Program score.py
# Author: ...

class Score:
	"""A score for mastermind
	   A black peg is correct color in correct position...
	"""

	def __init__(self, numBlack, numWhite):
		self._numBlack = numBlack
		self._numWhite = numWhite

	def getNumBlack(self):
		return self._numBlack

	def getNumWhite(self):
		return self._numWhite