from cs1graphics import *

screen = Canvas(400,400)

ball = Circle(30)
ball.setFillColor('red')
ball.setBorderColor('red')
screen.add(ball)

xVelocity = 9
yVelocity = 0

gravity = 1

while(1):
	yVelocity = gravity + yVelocity
	ball.move(xVelocity,yVelocity)
	screen.refresh()