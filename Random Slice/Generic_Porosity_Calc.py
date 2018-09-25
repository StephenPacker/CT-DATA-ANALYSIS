# This porosity calculator is designed to work with essentially any shape, assuming the scan only has one sample, and
# that the sample is relatively closed (Picture pouring water on top of the provided images, if the water flows around
# the image that means the porosity calc should be accurate, if the water flows though the image the accuracy will
# likely be much lower). In exchange for generality of shape, the computation time is much slower.

import glob
import cv2
import numpy as np


def main():

	images = file_reader()

	porosities = np.empty(len(images))

	for i in range(len(images)):
		total_img_pixels = 0
		total_shape_pixels = 0
		shape = shape_outliner(images[i])
		total_img_pixels += np.count_nonzero(images[i])
		total_shape_pixels += np.count_nonzero(shape)
		porosities[i] = por_calc(total_img_pixels, total_shape_pixels)

	porosity_avg = 0

	for j in range(len(porosities)):
		porosity_avg += porosities[j]

	print(porosity_avg/len(porosities))


# Absolutely brute force implementation that transposes the outline or shape of our data set onto a blank array that
# can be referenced as an alternative to assuming all objects are circular in form. Essentially carves the general shape
# Into a new 3D array! If run time is already slow, then fuck it!
def shape_outliner(image):

	width = image.shape[0]
	height = image.shape[1]
	shape = np.ones((width, height), dtype=int)
	cur_i = image

	# Move left to right
	for j in range(0, height):
		width_index = width - 1
		height_index = j
		cur_p = cur_i[width_index, height_index]
		while cur_p == 0 and width_index > 0:
			width_index -= 1
			cur_p = cur_i[width_index, height_index]
			shape[width_index, height_index] = 0

	# Move right to left
	for j in range(0, height):
		width_index = 0
		height_index = j
		cur_p = cur_i[width_index, height_index]
		while cur_p == 0 and width_index < width - 1:
			width_index += 1
			cur_p = cur_i[width_index, height_index]
			shape[width_index, height_index] = 0

	shape = cv2.medianBlur(shape.astype(np.float32), 5)

	return shape


def por_calc(bright_pixels, total_pixels):
	return (1 - (bright_pixels/float(total_pixels))) * 100


# Reads in image files specified by the users
def file_reader():
	while True:
		file_location = raw_input("Please specify the file path to where your images are stored: ")
		file_type = raw_input("Please specify the file type. I.e bmp: ")
		files = (glob.glob(file_location + "/*." + file_type))
		images = []
		for img_file in files:
			images.append(cv2.imread(img_file, 0))
		if len(images) == 0:
			print("The folder location or file type you selected were invalid, please try again")
			continue
		break

	return images


main()
