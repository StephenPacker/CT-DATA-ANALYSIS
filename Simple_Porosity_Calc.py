# A porosity calculator that is designed to work with circular, irregular shapes, only ten circles are made and the
# largest one is taken to represent the entire data set. Seems to do a really good job measuring porosity for whatever
# reason

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

	for i in range(0, len(images), int(math.floor(len(images) // 10))):  # Take one measurement each tenth
		width_index = width
		cur_i = images[i]
		cur_p = cur_i[center[1], width - 1]  # Start on the right hand boundary

		while cur_p == 0 and width_index > 0:  # Continue iterating until we hit our data set, maxes out at left edge
			width_index -= 1
			cur_p = cur_i[center[1], width_index]
		radii.append(width_index - center[0])

	total_nonzero_pixels = 0

	for i in range(len(images)):
		total_nonzero_pixels += np.count_nonzero(images[i])

	total_porosity = por_calc(total_nonzero_pixels, (math.pi * (max(radii) ** 2)) * i)
	print(total_porosity)


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

