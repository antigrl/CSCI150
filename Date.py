class Date:

	monthNames = (
		'January','February','March','April','May',
		'June','July','August','September','October',
		'November','December'
		)
	monthLengths = (31,28,31,30,31,30,31,31,30,31,30,31)

	def __init__(self,month, day, year):
		self._month = month
		self._day = day
		self._year = year

	def getDay(self):
		return self._day

	def setYear(self, yr):
		self._year = yr

	def __str__(self):
		return Date.monthNames[self._month-1] + ' ' \
		+ str(self._day) + ', ' + str(self._year)

	def upDate(self):
		self._day += 1
		if self._day > self.monthLength(self._month):
			self._month += 1
			self._day = 1
			if self._month == 13:
				self._year += 1
				self._month = 1

	def monthLength(self,month):
		if self._month == 2 and self._year %4 == 0:
			return 29
		else:
			return Date.monthLengths[self._month-1]





		



if __name__ == "__main__":
	theNextDay = Date(12,31,2000)
	theNextDay.upDate()

	print theNextDay