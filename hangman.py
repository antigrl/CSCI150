from cs1graphics import *
import random

screen = Canvas(640,640)

gallows = Path([
		Point(250,500),
		Point(450,500),
		Point(450,40),
		Point(250,40),
		Point(250,100)
	])

head = Circle(30)
head.move(250,130)
body = Path([
		Point(250,160),
		Point(250,300)
	])

leftArm = Path([
		Point(175,150),
		Point(250,195)
	])

rightArm = Path([
		Point(325,150),
		Point(250,195)
	])

leftLeg = Path([
		Point(325,400),
		Point(250,300)
	])

rightLeg = Path([
		Point(175,400),
		Point(250,300)
	])

parts = [head,body,leftArm,rightArm,leftLeg,rightLeg]

screen.add(gallows)


print 'Let\'s play hangman!'

secretWord = random.choice([
		'trumpet',
		'clarinet',
		'drums',
		'flute',
		'saxophone',
	])
guesses = []
turns = 6

while turns > 0:
	missed = 0
	for letter in secretWord:
		if letter in guesses:
			print letter,
		else:
			print '_',
			missed += 1

	print

	
	if missed == 0:
		print 'You win!'
		break

	guess = raw_input('Guess a letter: ')
	guesses += guess

	if guess not in secretWord:
		turns -= 1
		print 'Wrong!'
		screen.add(parts[turns])
		print turns, 'more turns'
		if turns == 0:
			print 'The answer is', secretWord
