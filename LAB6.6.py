collection = ['three','three','seven','twenty','four','three','eleven']
value = 'three'

def count(self,value):
	count = 0
	for object in self:
		if object == value:
			count += 1
	return count

print count(collection,value)
		