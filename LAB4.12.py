people = ['Bob Ward', 'Kim Walta', 'John Adams', 'Steven Johnson']
lastNameFirst = []
sortedPeople = []

for person in people:
	nameSeparate = person.split()
	lastNameFirst.append(nameSeparate[1]+' '+nameSeparate[0])


lastNameFirst.sort();

for person in lastNameFirst:
	nameSeparate = person.split()
	print nameSeparate[1],nameSeparate[0]
