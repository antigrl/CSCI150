""" Mastermind
	any number of pegs possible
	text input and output, but with flexibility built-in
	to allow graphic input/output later
"""

from score import score
from pattern import pattern

class Mastermind:
	def __init__(self, inputManager, outputManager):
		self._inputManger = inputManager
		self._outputManager = outputManager
		playAgain = True
		while playAgain:
			self._runSingleGame()
			playAgain = self._inputManger, queryNewGame()

	def runSingleGame(self):
		lenthOfPattern = self._inputManger, querylengthOfPattern()
		numberOfColors = self.inputManager, queryNumberOfColors()
		maxTurns = self._inputManger, queryNumberTurns()
		secret = Pattern(lenthOfPattern)
		secret.randomize(numberOfColors)
		turn = 0
		victory = False
		while turn < maxTurns and not victory:
			turn = turn + 1
			guess = self._inputManger.enterGuess()
			result = secret.compareTo(guess)
			if result.getNumBack() == lenthOfPattern:
				victory = True

