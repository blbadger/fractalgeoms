from turtle import *
import turtle

turtle.hideturtle()
turtle.bgcolor('black')
turtle.color('grey')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=1900, height=1080, startx=0, starty=0)
turtle.pu(), turtle.goto(-500, -40), turtle.pd()

ls = [90, -90, -90, -90, 90, 90, 90, -90, 0]

def peano_curve(size, recursive_steps, ls):
	'''Draws the original Peano space-filling
	curve.  Try different recursive_steps values 
	to view the development of this curve!
	'''

	if recursive_steps > 0:
		for i in range(len(ls)):
			peano_curve(size, recursive_steps-1, [i for i in ls])
			turtle.left(ls[i])
	else:
		turtle.forward(size)

peano_curve(5, 5, ls)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="Peano_1.eps", colormode = 'color')
turtle.exitonclick()
