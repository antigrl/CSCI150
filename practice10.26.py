filename = raw_input('What is a filename? ')
# recall default is to open for reading
source = file(filename)

numlines = 0
numchars = 0
numwords = 0
line = source.readline()
while line:
	numlines = numlines + 1
	numwords = numwords + len(line.split())
	numchars = numchars + len(line)


print numlines, numwords, numchars


