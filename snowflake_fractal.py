from turtle import *
import turtle

turtle.hideturtle()
turtle.bgcolor('black')
turtle.color('grey')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=2000, height=1000, startx=0, starty=0)
turtle.pu()
turtle.goto(-500, -400)
turtle.pd()
def snowflake_curve(size, recursive_steps):
	if recursive_steps > 0:
		for angle in [60, 60, -60, -60, -60, -60, 60, 60, 0]:
			snowflake_curve(size, recursive_steps-1)
			turtle.left(angle)

	else:
		turtle.forward(size)

snowflake_curve(1, 5)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="Snowflake_1.eps", colormode = 'color')
turtle.exitonclick()
