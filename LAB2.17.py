person = 'Kim Walta'

space = person.index(' ')
name = person[space+1:] + ', ' + person[:space]

print name