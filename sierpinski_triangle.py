from turtle import *
import turtle

turtle.hideturtle()
turtle.bgcolor('white')
turtle.color('grey')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
width = 1900
height = 1080
turtle.setup (width, height, startx=0, starty=0)

# fill the background (bgcolor does not save by itself using .postscript())
turtle.pu()
turtle.goto(-1000, -500)
canvas = turtle.getcanvas()
turtle.fillcolor(turtle.Screen().bgcolor())
turtle.begin_fill()

turtle.forward(width+2), turtle.left(90)
turtle.forward(height+2), turtle.left(90)
turtle.forward(width+2), turtle.left(90)
turtle.forward(height+2), turtle.left(90)
turtle.end_fill()

#reposition starting point
turtle.pu()
turtle.goto(-700, -400)
turtle.pd()

ls = [60, 60, -60, -60, -60, -60, 60, 60, 0]
def sierpinski_curve(size, recursive_steps, ls):
	if recursive_steps == 0:
		turtle.forward(size)
	else:
		for i in range(len(ls)):
			if i % 2 == 0:
				sierpinski_curve(size, recursive_steps-1, [i for i in ls])
				turtle.left(ls[i])
			else:
				sierpinski_curve(size, recursive_steps-1, [-i for i in ls])
				turtle.left(ls[i])

running = True
frames_per_second = 5
counter = 1

def save(counter):
	# saves the canvas as a vector .eps file at the designated frame rate
    getcanvas().postscript(file = "drawing{0:03d}.eps".format(counter[0], colormode = 'color'))
    counter[0] += 1
    if running:
        ontimer(save, int(1000 / frames_per_second))

counter = [1]
save(counter)  

ontimer(sierpinski_curve(1, 5, ls), 500) 

running = False

done()