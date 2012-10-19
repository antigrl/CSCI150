from cs1graphics import *

screen = Canvas()
green = Circle(20)
green.setFillColor('green')
green.move(100,50)


yellow = Circle(20)
yellow.setFillColor('yellow')
yellow.move(100,100)


red = Circle(20)
red.setFillColor('red')
red.move(100,150)


screen.add(green)
green.wait()
screen.remove(green)

screen.add(yellow)
yellow.wait()
screen.remove(yellow)

screen.add(red)
red.wait()
screen.remove(red)