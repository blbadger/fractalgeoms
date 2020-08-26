from turtle import *
import turtle

class Cantor_drawing:
	'''Draws a Cantor set with red and blue vertical lines
	on a black background using turtle.  
	'''

	def __init__(self, size, recursive_steps, width, height, color):
		self.size = size
		self.recursive_steps = recursive_steps
		self.width = width
		self.height = height
		self.color = color

	def cantor_set(self):
		# Draws the cantor set recursively
		if self.recursive_steps > 0:
			# only proceed if not out of canvas bounds
			if turtle.pos()[0] < self.width:
				self.size /= 3
				self.recursive_steps -= 1
				Cantor_drawing.cantor_set(self)
				self.size *= 3
				self.recursive_steps += 1
			turtle.pu()
			turtle.forward(self.size)
			turtle.pd()

			# only proceed if not out of canvas bounds
			if turtle.pos()[0] < self.width:
				self.size /= 3
				self.recursive_steps -= 1
				Cantor_drawing.cantor_set(self)
				self.size *= 3
				self.recursive_steps += 1

		else:
			turtle.color('blue')
			turtle.left(90)
			turtle.forward(self.height), turtle.right(180), turtle.forward(self.height)
			turtle.left(90)
			turtle.pu(), turtle.forward(self.size), turtle.pd()
			turtle.color('red')
			turtle.left(90)
			turtle.forward(self.height), turtle.right(180), turtle.forward(self.height)
			turtle.left(90)


	def background_rect(self):
		# draw a background rectangle and fill with desired color
		turtle.goto(-self.width//2 - 1, -self.height//2 - 1)
		turtle.fillcolor(self.color)

		turtle.begin_fill()
		turtle.forward(self.width+2), turtle.left(90)
		turtle.forward(self.height+2), turtle.left(90)
		turtle.forward(self.width+2), turtle.left(90)
		turtle.forward(self.height+2), turtle.left(90)
		turtle.end_fill()
		turtle.forward(100)


for i in range(300):
	turtle.hideturtle()
	turtle.bgcolor('black'), turtle.color('black')
	turtle.speed(0), turtle.delay(0)
	turtle.pensize(0.001)

	w, h = 1900, 1080 # width and height
	turtle.setup (width=w, height=h, startx=0, starty=0)
	turtle.pu()
	turtle.goto(-900, -540)
	turtle.pd()
	Cantor_drawing(500, 5, w, h, 'black').background_rect()
	Cantor_drawing(500 * (2**(i/30)), 5 + i // 30, w, h, 'black').cantor_set()

	turtle_screen = turtle.getscreen()
	turtle_screen.getcanvas().postscript(file="cantor_set{0:03d}.eps".format(i))
	turtle.reset()
