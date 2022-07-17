from PIL import Image
import os

path = '/home/bbadger/Desktop/endocytosis_fractal/'


def image_converter(path):
	files = os.listdir(path)
	for i in range(1, len(files)):
		print ('endocytosis{0:03d}.eps'.format(i))
		string = str(i)
		while len(string) < 3:
			string = '0' + string
		try:
			eps_image = Image.open(path + 'endocytosis{0:03d}.eps'.format(i))
		except:
			break
		eps_image.load(scale=2)   
		eps_image.save(path + 'endocytosis{0:03d}.png'.format(i)) 

	return


path = '/home/bbadger/Desktop/snowflake/'

def image_deleter(path):
	files = os.listdir(path)
	for i in range(2, 500):
		string = str(i)
		while len(string) < 3:
			string = '0' + string
		try:
			path2 = path + 'endocytosis_vid' + string + '.eps'
			print (path2)
			os.remove(path2, dir_fd=None)
		except:
			break

	return

