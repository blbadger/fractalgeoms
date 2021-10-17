from turtle import *
import turtle
import random

a = (-400,-400)
b = (-400, 400)
c = (400, -400)
d = (400, 400)
div1 = 0
div2 = 1

def randomized_sierpinski(steps, a, b, c, d, div1, div2):
	for i in range(steps):
		pos = [j for j in turtle.pos()]

		n = random.randint(0, 8)
		turtle.pu()
		if n < 2:
			turtle.goto(pos[0]*div1+a[0]*div2, pos[1]*div1+a[1]*div2)

		elif n >= 6:
			turtle.goto(pos[0]*div1+b[0]*div2, pos[1]*div1+b[1]*div2)

		elif n < 6 and n >= 4:
			turtle.goto(pos[0]*div1+c[0]*div2, pos[1]*div1+c[1]*div2)

		elif n < 4 and n >= 2:
			turtle.goto(pos[0]*div1 + d[0]*div2, pos[1]*div1 + d[1]*div2)

		turtle.pd()
		if i > 100:
			turtle.forward(0.5)

for i in range(0, 300):

	turtle.hideturtle()
	# turtle.bgcolor('black')
	# turtle.color('white')
	turtle.speed(0)
	turtle.delay(0)

	turtle.pensize(2)
	width = 1900
	height = 1080
	turtle.setup (width, height, startx=0, starty=0)

	# fill the background (bgcolor does not save by itself using .postscript())
	# turtle.pu()
	# turtle.goto(-1000, -500)
	# canvas = turtle.getcanvas()
	# turtle.fillcolor(turtle.Screen().bgcolor())
	# turtle.begin_fill()

	# turtle.forward(width+2), turtle.left(90)
	# turtle.forward(height+2), turtle.left(90)
	# turtle.forward(width+2), turtle.left(90)
	# turtle.forward(height+2), turtle.left(90)
	# turtle.end_fill()

	#reposition starting point
	# turtle.pu()
	# turtle.goto(-550, -400)
	# turtle.pd()

	# turtle.Vec2D() to convert to turtle vector

	print (i)
	randomized_sierpinski(5000, a, b, c, d, div1 + i/300, div2 - i/300)
	turtle_screen = turtle.getscreen()
	turtle_screen.getcanvas().postscript(file="randomized_sierpinski{0:03d}.eps".format(i), colormode = 'color')
	turtle.reset()

# running = True
# frames_per_second = 1
# counter = 1

# def save(counter = [1]):
# 	# saves the canvas as a vector .eps file at the designated frame rate
#     getcanvas().postscript(file = "random_sierpinski{0:03d}.eps".format(counter[0], colormode = 'color'))
#     counter[0] += 1
#     if running:
#         ontimer(save, int(1000 / frames_per_second))

# save()  

# ontimer(randomized_sierpinski(300000, a, b, c), 500) 

# running = False

# done()
