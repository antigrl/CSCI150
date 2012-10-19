def __contains__(self,value):
	i = 0					# index-based search
	found = False			# pessimism
	while i < len(self) and not found:
		if self[i] == val:
			found = True	# found it
		else:
			i += 1			# keep looking
		return found		