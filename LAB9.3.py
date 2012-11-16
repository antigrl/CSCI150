import Person

class Student(Person):
	"""Rewrite the Student class as a child class of Person, reusing as much of the Person class functionality as possible.
	"""

	def __init__(self, id):
		Person.__init__(self, name, age)					# call the parent constructor
		self.id = id

	def printInfo(self):
		person.printInfo(self)
		print 'ID:', self.id