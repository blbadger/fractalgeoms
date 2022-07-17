from turtle import *
import turtle

turtle.hideturtle()
turtle.bgcolor('white')
turtle.color('black')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=1400, height=1000, startx=0, starty=0)

width = 1600
height = 1000
turtle.pu()
turtle.goto(-1000, -540)
canvas = turtle.getcanvas()
turtle.fillcolor(turtle.Screen().bgcolor())
turtle.begin_fill()

turtle.forward(width+1000), turtle.left(90)
turtle.forward(height+1000), turtle.left(90)
turtle.forward(width+1000), turtle.left(90)
turtle.forward(height+1000), turtle.left(90)
turtle.end_fill()


turtle.pu()
turtle.goto(-400,-300)
turtle.pd()
def endocytic_curve(size, recursive_steps):
	if recursive_steps > 0:
		for angle in [60, -60, -60]:
			turtle.left(angle)
			endocytic_curve(size, recursive_steps-1)
		turtle.left(60)
	else:
		turtle.forward(size)


running = True
frames_per_second = 2
counter = 1

def save(counter=[1]):
	# saves the canvas as a vector .eps file at the designated frame rate
	getcanvas().postscript(file = "endocytic_vid{0:03d}.eps".format(counter[0], colormode = 'color'))
	counter[0] += 1
	if running:
		ontimer(save, int(1000 / frames_per_second))


save()  

ontimer(endocytic_curve(0.7, 10), 500) 

running = False

done()

# endocytic_curve(50, recursive_steps = 4)
# turtle_screen = turtle.getscreen()
# turtle_screen.getcanvas().postscript(file="endocytosis_1.eps", colormode = 'color')
# getcanvas().postscript(file = "endocytosis{0:03d}.eps".format(4, colormode = 'color'))
# turtle.exitonclick()