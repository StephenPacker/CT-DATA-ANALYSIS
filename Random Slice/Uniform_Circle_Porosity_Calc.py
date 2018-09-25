# A porosity calculator that is designed to work with circular, highly regular shapes, each image gets its own circular
# border and the porosity is based on the ratio of bright pixels within the circle, and the volume of the circle itself.

import glob
import cv2
import numpy as np
import math


def main():

	images = file_reader()

	width = images[1].shape[0]
	height = images[1].shape[1]
	center = (int(width // 2), int(height // 2))

	radii = []
	porosity_holder = []

	for i in range(0, len(images)):
		width_index = width
		cur_i = images[i]
		cur_p = cur_i[center[1], width - 1]

		while cur_p == 0 and width_index > 0:
			width_index -= 1
			cur_p = cur_i[center[1], width_index]
		radius = (width_index - center[0])
		porosity_holder.append(por_calc(np.count_nonzero(images[i]), (math.pi * (radius ** 2))))
		radii.append(radius)

	total_porosity = 0
	for porosities in porosity_holder:

		total_porosity += porosities

	print(total_porosity / len(porosity_holder))


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