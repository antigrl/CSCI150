class OurList:
	def __init__(self):
		self._head = None
		self._rest = None

	def _isEmpty(self):
		return self._rest = None

	def append(self, value):
		if self._isEmpty():
			self._head = value
			self._rest = OurList()
		else:
			self._rest.append(value)