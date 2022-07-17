from turtle import *
import turtle

turtle.hideturtle()
# turtle.bgcolor('black')
turtle.color('black')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=1200, height=1000, startx=0, starty=0)
turtle.pu()
turtle.goto(-480, -100)
turtle.pd()
ls = [60, -120, 60, 0]
def koch_curve(size, recursive_steps, ls):
	if recursive_steps > 0:
		for i in range(len(ls)):
			koch_curve(size, recursive_steps-1, [i for i in ls])
			turtle.left(ls[i])

	else:
		turtle.forward(size)

koch_curve(1.3, 6, ls)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="koch_snowflake6.eps", colormode = 'color')
turtle.exitonclick()

# 50, 2