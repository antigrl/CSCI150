#! /usr/bin/python
import random
import time
from cs1graphics import *

# Set Canvas size
screen = Canvas(600,400)

# Empty list
balls = []

# Define ball as a circle object with the velocity of 10
def add_ball():
	ball = {
			'object':Circle(),
			'x_velocity':10,
			'y_velocity':10,
			'growing':False
		}
	# Move the ball object randomly across the canvas
	ball['object'].moveTo(
		 	random.randint(0,600),
			random.randint(0,400)
		)
	# Make the ball red, add it to the canvas and add it to the balls list
	ball['object'].setFillColor('red')
	ball['object'].setRadius(8)
	ball['object'].setBorderWidth(0)
	screen.add( ball['object'] )
	balls.append(ball)

# For each ball in balls list, move them at set velocity
def update_balls():
	for ball in balls:
		ball['object'].move(
				ball['x_velocity'],
				ball['y_velocity']
			)

		# Get reference point of ball
		ball_x = ball['object'].getReferencePoint().getX()
		ball_y = ball['object'].getReferencePoint().getY()

		# If the ball hits a wall, it moves in the opposite direction and make it grow by 10
		if ball_x <= 0:
			ball['x_velocity'] = ball['x_velocity'] * -1
			ball['object'].setRadius(
				ball['object'].getRadius()+10)
		if ball_x >= 600:
			ball['x_velocity'] = ball['x_velocity'] * -1
			ball['object'].setRadius(
				ball['object'].getRadius()+10)
		if ball_y <= 0:
			ball['y_velocity'] = ball['y_velocity'] * -1
			ball['object'].setRadius(
				ball['object'].getRadius()+10)
		if ball_y >= 400:
			ball['y_velocity'] = ball['y_velocity'] * -1
			ball['object'].setRadius(
				ball['object'].getRadius()+10)
		
		# Increase the growing ball by 3
		if ball['growing']:
			ball['object'].setRadius(
				ball['object'].getRadius()+3)

# Register mouseclick event
class MouseClickHandler(EventHandler):
	def __init__(self):
		EventHandler.__init__(self)
		print "Initialized the mouse click handler"
		self.ball = None

	def handle(self,event):
		print "Event"

		if event.getDescription() == 'mouse click':
			print "Mouse Click"

			# Grow clicked ball at mouse location
			ball = {
				'object':Circle(5, event.getMouseLocation()),
				'x_velocity':0,
				'y_velocity':0,
				'growing':True
			}

			ball['object'].setFillColor('red')
			ball['object'].setBorderWidth(0)

			self.ball = ball

			# Add growin ball to canvas
			screen.add(ball['object'])

		# When mouse is released, ball stops growing and stays
		if event.getDescription() == 'mouse release':
			print "Mouse Release"

			self.ball['growing'] = False
			self.ball = None

# Add three balls
add_ball()
add_ball()
add_ball()

# Creates an instance of the mouse click handler
mouseClickHandler = MouseClickHandler()

# Add mouse click handler to the canvas
screen.addHandler( mouseClickHandler )

while(1):
	update_balls()
	screen.refresh()
	time.sleep(0)

# The monitor and timer classes aren't in the newest cs1graphics library.
# How do I give up control to handle mouse events?


