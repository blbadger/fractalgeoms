from turtle import *
import turtle

turtle.hideturtle()
# turtle.bgcolor('black')
# turtle.color('gray')
turtle.speed(0)
turtle.delay(0)

turtle.pensize(0.2)
turtle.setup (width=1500, height=1000, startx=0, starty=0)
turtle.pu()
turtle.goto(-700, -300)
turtle.pd()
ls = [0, 85, -170, 85]
def cesaro_sweep(size, recursive_steps, ls):
	if recursive_steps > 0:
		for i in range(len(ls)):
			turtle.left(ls[i])
			cesaro_sweep(size, recursive_steps-1, [i for i in ls])

	else:
		turtle.forward(size)

cesaro_sweep(10, 6, ls)
turtle_screen = turtle.getscreen()
turtle_screen.getcanvas().postscript(file="Cesaro_sweep1.eps", colormode = 'color')
turtle.exitonclick()
