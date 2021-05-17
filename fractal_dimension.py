# fractal_dimension.py 
# calculates the box counting dimension for thresholded images

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import os

def box_dimension(image_array, min_resolution, max_resolution):
	"""
	Takes an input array (converted from image) of 0s and 
	1s and returns the calculated box counting dimension
	over the range 5x to 500x scale
	"""
	assert max_resolution <= min(len(image_array), len(image_array[0])), 'resolution too high'

	counts_array = []
	scale_array = []
	y_size = len(image_array)
	x_size = len(image_array[0])
	for i in range(min_resolution, max_resolution, 10):
		scale_array.append(i)
		count = 0
		for j in range(0, y_size - i, i):
			for k in range(0, x_size - i, i):
				if check_presence(image_array, i, j, k):
					count += 1
		counts_array.append(count)

	# log transform scales and counts
	counts_array = [np.log(i) for i in counts_array]
	scale_array = [np.log(i) for i in scale_array]
	m, b = np.polyfit(scale_array, counts_array, 1) # fit a first degree polynomial
	return m, counts_array, scale_array


def check_presence(image_array, i, j, k):
	"""
	Checks for the presence of 1 in a square subarray
	of length i with top left coordinates (j, k).  Returns
	a boolean indicating presence.
	"""
	for x in range(i):
		for y in range(i):
			if image_array[j+y][k+x] == 1:
				return True

	return False

path = '/home/bbadger/Desktop/snowflake/snowflake752.png'

image_array = np.asarray(Image.open(path))
image_ls = []
for i in range(len(image_array)):
	temp = []
	for j in range(len(image_array[i])):
		temp.append(1 if any(image_array[i][j]) > 0 else 0)
	image_ls.append(temp)

m, counts_array, scale_array = box_dimension(image_ls, 20, 1500)
print (f'Fractal dimension: {-m}')

plt.scatter(scale_array, counts_array)
plt.show()
plt.close()














