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

	def __len__(self):
		if self._isEmpty():
			return 0
		else:
			return 1 + self._rest.__len__()

	def count(self, value):
		if self._isEmpty():
			return 0
		else:
			if self._head == value:
				return 1 + self._rest.count(value)
			else:
				return 0 + self._rest.count(value)

	def __contains__(self, value):
		if self._isEmpty():
			return False
		else:
			if self._head == value:
				return True
			else:
				return self._rest.__contains__(value)