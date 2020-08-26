from turtle import *
import turtle

def cantor_set(size, recursive_steps, width, height):
	if recursive_steps > 0:
		# only proceed if not out of canvas bounds
		if turtle.pos()[0] < width:
			cantor_set(size/3, recursive_steps-1, width, height)
		turtle.pu()
		turtle.forward(size)
		turtle.pd()

		# only proceed if not out of canvas bounds
		if turtle.pos()[0] < width:
			cantor_set(size/3, recursive_steps-1, width, height)

	else:
		turtle.color('blue')
		turtle.left(90)
		turtle.forward(height), turtle.right(180), turtle.forward(height)
		turtle.left(90)
		turtle.pu(), turtle.forward(size), turtle.pd()
		turtle.color('red')
		turtle.left(90)
		turtle.forward(height), turtle.right(180), turtle.forward(height)
		turtle.left(90)


def background_square(width, height, color):
	turtle.goto(-width//2 - 1, -height//2 - 1)
	turtle.fillcolor(color)

	# draw a background rectangle and fill with desired color
	turtle.begin_fill()
	turtle.forward(width+2), turtle.left(90)
	turtle.forward(height+2), turtle.left(90)
	turtle.forward(width+2), turtle.left(90)
	turtle.forward(height+2), turtle.left(90)
	turtle.end_fill()


for i in range(300):
	turtle.hideturtle()
	turtle.bgcolor('black'), turtle.color('black')
	turtle.speed(0), turtle.delay(0)
	turtle.pensize(0.001)

	w, h = 1900, 1080 # width and height
	turtle.setup (width=w, height=h, startx=0, starty=0)
	background_square(w, h, 'black')
	
	turtle.pu()
	turtle.goto(-900, -540)
	turtle.pd()

	cantor_set(500*2**(i/60), 5 + i//90, w, h)
	turtle_screen = turtle.getscreen()
	turtle_screen.getcanvas().postscript(file="cantor_set{0:03d}.eps".format(i))
	turtle.reset()
	