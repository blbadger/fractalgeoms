from turtle import *
import turtle

turtle.hideturtle()
# turtle.bgcolor('black')
turtle.color('black')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=1000, height=1000, startx=0, starty=0)
turtle.pu()
turtle.goto(-420, 0)
turtle.pd()
ls = [90, -90, -90, 0, 90, 90, -90, 0]
def koch_curve(size, recursive_steps, ls):
	if recursive_steps > 0:
		for i in range(len(ls)):
			koch_curve(size, recursive_steps-1, [i for i in ls])
			turtle.left(ls[i])

	else:
		turtle.forward(size)

koch_curve(0.8, 6, ls)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="koch_6.eps", colormode = 'color')
turtle.exitonclick()

# 50, 2