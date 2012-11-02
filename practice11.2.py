class OurList:

	def __init__(self):
		self._head = None  # data at the spot, None = Empty
		self._rest = None  # reference to everything else after this item

	def _isEmpty(self):
		return self._rest is None

	def append(self,value):
		if self._isEmpty():
			self._head = value
			self._rest = OurList()
		else:
			self._rest.append(value)

	def __len__(self):
		if self._isEmpty():
			return 0
		else:
			return 1 + len(self._rest)

	def __getitem__(self,i):
		if self._isEmpty():
			raise IndexError('List index out of range'):
		elif i == 0:
			return self._head
		else: return self._rest[i-1]

	def insert(index,value):
		if self._isEmpty():
			self._head = value
			self._rest = OurList()
		elif index == 0:
			shift = OurList()
			shift._head = self._head
			shift._rest = self._rest
			self._head = value
			self._rest = shift

	def min(self):
		if self._isEmpty():
			return None
		else:
			m = self._rest.min()
			if m is None or self._head < m:
				return self._head
			else:
				return m

	def remove(self,value):
		if self._isEmpty():
			raise ValueError()
		elif self._head == value:
			self._head = self._rest._head
			self._rest = self._rest._rest
		else:
			self._rest.remove(value)

	def sort(self):  # Bubble sort
		if self._isEmpty():
			pass
		else:
			m = self.min()
			if m != self._head:
				self.remove(m)
				self.insert(1,self._head)
				self._head = m







		