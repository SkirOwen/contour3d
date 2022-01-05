from typing import Tuple, List, Any
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

from tqdm import tqdm

from PIL import Image
from numpy import ndarray


def get_palette(max_height: int, min_height: int, contour_dist: int) -> Tuple[List[int], ndarray]:
	height_array = np.arange(min_height-contour_dist, max_height+contour_dist, contour_dist)
	palette_id = [i for i in range(1, len(height_array) + 1)]
	palette_id.remove(44)
	return np.array(palette_id), height_array


def load_img(file: str) -> np.ndarray:
	im = Image.open(file)
	return np.asarray(im)


def parse_contour(img: np.ndarray, palette_id: List, height_array: ndarray) -> tuple[ndarray, int, int]:
	height, width, clr = img.shape

	contour = np.zeros((height, width))

	for x in tqdm(range(width)):
		for y in range(height):
			pixel_val = img[y, x, 0]

			# if pixel_val in [255, 0, 92, 44, 45, 104, 156, 46]:
			# 	continue

			try:
				contour[y, x] = height_array[np.where(palette_id == pixel_val)]
			except ValueError:
				continue

	return contour, height, width


def plot_3d(contour, height: int, width: int) -> None:

	x = np.array([x for x in range(width)])
	y = np.array([x for x in range(height)])
	X, Y = np.meshgrid(x, y)

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.contour3D(X, Y, contour)

	plt.show()


def main():
	min_height = 1280
	max_height = 2120
	contour_dist = 20
	palette_id, height_array = get_palette(max_height, min_height, contour_dist)

	img = load_img("./colour_map.PNG")

	parse_contour(img, palette_id, height_array)


if __name__ == '__main__':
	main()
	#
	# palette = get_palette(2120, 1280, 20)
	# print(palette)





