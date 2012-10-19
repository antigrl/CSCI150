collection = ['three','three','seven','twenty','four','three','eleven']
value = 'three'

def replace(self,old,new):

	for i in range(len(self)):
		if self[i] == old:
			self[i] = new

replace(collection,'four','three')
print collection