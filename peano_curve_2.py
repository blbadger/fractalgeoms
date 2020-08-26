from turtle import *
import turtle

turtle.hideturtle()
turtle.bgcolor('black'), turtle.color('gray')
turtle.speed(0), turtle.delay(0)

turtle.pensize(1)
turtle.setup (width=2000, height=1080, startx=0, starty=0)
turtle.pu(), turtle.goto(-400, -400), turtle.pd()

def peano_curve(size, steps, orientation):
	X = 'XFYFX+F+YFXFY-F-XFYFX'
	Y = 'YFXFY-F-XFYFX+F+YFXFY'
	l = r = 90

	if steps == 0:
		return

	if orientation > 0:
		for i in X:
			if i == 'X':
				peano_curve(size, steps-1, orientation)
			elif i == 'Y':
				peano_curve(size, steps-1, -orientation)
			elif i == '+':
				turtle.left(90)
			elif i == '-':
				turtle.right(90)
			else:
				turtle.forward(size)

	else:
		for i in Y:
			if i == 'X':
				peano_curve(size, steps-1, -orientation)
			elif i == 'Y':
				peano_curve(size, steps-1, orientation)
			elif i == '+':
				turtle.left(90)
			elif i == '-':
				turtle.right(90)
			else:
				turtle.forward(size)



peano_curve(10, 4, 1)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="Noncontacting_Peano_curve.eps", colormode = 'color')
turtle.exitonclick()



