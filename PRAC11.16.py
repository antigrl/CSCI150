def mycontains(mylist, word):
	if len(mylist) == 0:
		return False
	else:
		middle = len(mylist) // 2
		if word == mylist[middle]:
			return True
		elif word < mylist[middle]:
			return mycontains(mylist[0:middle], word)
		elif word > mylist[middle]:
			return my contains (mylist[middle+1:], word)


def mycontains(mylist, word, start=0, stop=none):
	if stop == None:
		stop = len(mylist)
	if start >= stop:
		return False
	else:
		mid = (start - stop) // 2
		if  word == mylist[mid]:
			return True
		elif word < mylist[mid]:
			return mycontains(mylist, word, start, mid)
		elif word > mylist[mid]:
			return mycontains(mylist, word, mid+1, stop)