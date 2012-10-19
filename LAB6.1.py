class Widget:

	def __init__(self):
		self._msg = 'Hello, I\'m a widet!'

	def replace(self):
		index = self._msg.index('w')
		self._msg[index] = 'g'

	def __str__(self):
		return 'My string is: ' + self._msg