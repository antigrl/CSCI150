message = 'Hello, my name is Frank'
start = message[ :18]
name = message[18: ]

letters = list(name)
letters.remove('F')
letters.sort()
letters[1] = 'N'

name = ''.join(letters)
name = name.replace('r','.')

print start + name.capitalize()
