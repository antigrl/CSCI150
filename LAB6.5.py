class Date:

	monthNames = ('January','February','March','April','May','June','July','August','September','October','November','December')

	def __init__(self):
		# By default: January 1, 2000
		self._month = 1
		self._day = 1
		self._year = 2000

	def getDay(self):
		return int(self._day)

	def setYear(self):
		return self._year

	def __str__(self):
		return str('January 1, 2000')