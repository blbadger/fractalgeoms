from turtle import *
import turtle as t

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
			if t.pos()[0] < self.width:
				self.size /= 3
				self.recursive_steps -= 1
				self.cantor_set()
				self.size *= 3
				self.recursive_steps += 1
			t.pu()
			t.forward(self.size)
			t.pd()

			# only proceed if not out of canvas bounds
			if t.pos()[0] < self.width:
				self.size /= 3
				self.recursive_steps -= 1
				self.cantor_set()
				self.size *= 3
				self.recursive_steps += 1

		else:
			t.color('blue')
			t.left(90)
			t.forward(self.height), t.right(180), t.forward(self.height)
			t.left(90)
			t.pu(), t.forward(self.size), t.pd()
			t.color('red')
			t.left(90)
			t.forward(self.height), t.right(180), t.forward(self.height)
			t.left(90)


	def background_rect(self):
		# draw a background rectangle and fill with desired color
		t.goto(-self.width//2 - 1, -self.height//2 - 1)
		t.fillcolor(self.color)

		t.begin_fill()
		t.forward(self.width+2), t.left(90)
		t.forward(self.height+2), t.left(90)
		t.forward(self.width+2), t.left(90)
		t.forward(self.height+2), t.left(90)
		t.end_fill()
		t.forward(100)


for i in range(300):
	t.hideturtle()
	t.bgcolor('black'), t.color('black')
	t.speed(0), t.delay(0)
	t.pensize(0.001)

	w, h = 1900, 1080 # width and height
	t.setup (width=w, height=h, startx=0, starty=0)
	t.pu()
	t.goto(-900, -540)
	t.pd()
	background = Cantor_drawing(500, 5, w, h, 'black')
	background.background_rect()
	drawing = Cantor_drawing(500 * (2**(i/30)), 5 + i // 30, w, h, 'black')
	drawing.cantor_set()

	turtle_screen = t.getscreen()
	turtle_screen.getcanvas().postscript(file="cantor_set{0:03d}.eps".format(i))
	t.reset()
