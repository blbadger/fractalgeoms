from turtle import *
import turtle

turtle.hideturtle()
# turtle.bgcolor('black')
# turtle.color('white')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(2)
turtle.setup (width=2000, height=1000, startx=0, starty=0)
turtle.pu()
turtle.goto(-800, 0)
turtle.pd()
def cantor_set(size, recursive_steps):
	if recursive_steps > 0:
		cantor_set(size/3, recursive_steps-1)
		turtle.pu()
		turtle.forward(size)
		turtle.pd()
		cantor_set(size/3, recursive_steps-1)

	else:
		turtle.color('black')
		turtle.forward(size)
		turtle.pu()
		turtle.forward(size)
		turtle.pd()
		turtle.color('black')
		turtle.forward(size)

cantor_set(500, 3)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="cantor_set3.eps")
turtle.exitonclick()