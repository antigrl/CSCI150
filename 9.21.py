alive = true
while alive == True:
  input = raw_input('Which direction (N,S,E, or W): ')
  if input == 'N':
  	print 'You see a waterfall'
  if input == 'S':
  	print 'You come to a locked door'
  if input == 'E':
  	print 'You fall off a cliff'
  if input == 'W':
  	print 'You see a monster'
  if input == 'Q':
  	print 'Goodbye'
  	alive = False



 longwords = list()
 for x in words:
 	if len(x) > 3:
 		longwords.append(x)

 test = ['kevin','scannell','python','java','hi','java','java']

 for index in range(0,len(test)):
 	if test [index] == 'java':
 		text[index] = 'python'