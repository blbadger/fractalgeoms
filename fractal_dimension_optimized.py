# fractal_dimension_optimized.py 
# Calculates the box counting dimension for thresholded images
# using numpy, non-elementwise version

from PIL import Image, ImageOps
import numpy as np 
import matplotlib.pyplot as plt

path = '/home/bbadger/Desktop/blbadger.github.io-master/fractals/koch_snowflake6.png'

# make grayscale array for image
image = Image.open(path)
grayscale_image = ImageOps.grayscale(image)
image_array = np.asarray(grayscale_image)

def box_dimension(image_array, min_size, max_size):
	"""
	Takes an array representing a monocolor image,
	min_size (int), and max_size (int) as args and
	returns the box counting dimension m, along with
	arrays representing boxes filled per scale (r size).
	"""

	assert max_size < min(len(image_array), len(image_array[0])), 'max size too large'

	counts_array = []
	scale_array = []
	y_size = len(image_array)
	x_size = len(image_array[0])
	for i in range(min_size, max_size, 5):
		scale_array.append(i)
		count = 0
		for j in range(0, y_size - i, i):
			for k in range(0, x_size - i, i):
				field = image_array[j:j+i, k:k+i]
				# print (field)
				if any(any(row < 10) for row in field):
					count += 1

		counts_array.append(count)

	# log transform scales and counts
	counts_array = [np.log(i) for i in counts_array]
	scale_array = [np.log(i) for i in scale_array]
	m, b = np.polyfit(scale_array, counts_array, 1) # fit a first degree polynomial

	return m, counts_array, scale_array


m, counts_array, scale_array = box_dimension(image_array, 1, 500)
print (f'Fractal dimension: {-m}')

plt.scatter(scale_array, counts_array)
plt.xlabel('log r')
plt.ylabel('log N')
plt.show()
plt.close()








