from cs1graphics import *
from time import sleep
c = Canvas()
count = 0
click = c.wait()
circ = Circle(10, click.getMouseLocation())
circ.setFillColor('skyBlue')
c.add(circ)
vel = 0
while count < 25:
	vel = vel + 3
	circ.move(0, vel)
	count = count + 1
	sleep(0.1)