from turtle import *
import turtle
import random

turtle.hideturtle()
# turtle.bgcolor('black')
# turtle.color('white')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.5)
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
turtle.pu()
turtle.goto(-550, -400)
turtle.pd()

# turtle.Vec2D() to convert to turtle vector
a = (-400,-400)
b = (-400, 400)
c = (400, -300)

def randomized_sierpinski(steps, a, b, c):

	for i in range(steps):
		pos = [j for j in turtle.pos()]

		n = random.randint(0, 6)
		turtle.pu()
		if n < 2:
			turtle.goto((pos[0]+a[0])/2, (pos[1]+a[1])/2)

		elif n >= 4:
			turtle.goto((pos[0]+b[0])/2, (pos[1]+b[1])/2)

		else:
			turtle.goto((pos[0]+c[0])/2, (pos[1]+c[1])/2)

		turtle.pd()
		if i > 100:
			turtle.forward(0.5)


# randomized_sierpinski(30000, a, b, c)
# turtle_screen = turtle.getscreen()
# turtle_screen.getcanvas().postscript(file="sierpinski_0.eps", colormode = 'color')
# turtle.exitonclick()

running = True
frames_per_second = 1
counter = 1

def save(counter = [1]):
	# saves the canvas as a vector .eps file at the designated frame rate
    getcanvas().postscript(file = "random_sierpinski{0:03d}.eps".format(counter[0], colormode = 'color'))
    counter[0] += 1
    if running:
        ontimer(save, int(1000 / frames_per_second))

save()  

ontimer(randomized_sierpinski(300000, a, b, c), 500) 

running = False

done()