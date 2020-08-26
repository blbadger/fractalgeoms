from turtle import *
import turtle

def cantor_set(size, recursive_steps):
	if recursive_steps > 0:
		cantor_set(size/3, recursive_steps-1)

		turtle.pu(), turtle.forward(size), turtle.pd()
		cantor_set(size/3, recursive_steps-1)

	else:
		turtle.color('red'), turtle.forward(size)
		turtle.pu(), turtle.forward(size), turtle.pd()
		turtle.color('blue'), turtle.forward(size)


for i in range(300):
	turtle.hideturtle()
	turtle.speed(0), turtle.delay(0)
	turtle.pensize(4)
	turtle.setup (width=1900, height=1080, startx=0, starty=0)
	turtle.pu(), turtle.goto(-800, 0), turtle.pd()

	cantor_set(500 * (2**(i/30)), 4 + i // 30)
	turtle_screen = turtle.getscreen()
	turtle_screen.getcanvas().postscript(file="cantor_set{0:03d}.eps".format(i))
	turtle.reset()

