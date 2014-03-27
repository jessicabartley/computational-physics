from __future__ import division

from math import pi, sqrt
from random import random

AREA_OF_SQUARE = 4
NUMBER_OF_ITERATIONS = 50000


def generate_coordinates(no_of_dimensions):
	coordinates = []
	for i in range(no_of_dimensions):
		coordinates.append(2 * random() - 1)
	return coordinates


def find_length(x, y):
	length = sqrt(x ** 2 + y ** 2)
	return length


def is_within_circle(length):
	return length <= 1


def estimate_pi(total_iterations):
	no_of_hits = 0
	for i in range(total_iterations):
		coordinates = generate_coordinates(2)  # 2 dimensions only
		length = find_length(*coordinates)  # * means expands the tuple, also works for lists
		if is_within_circle(length):
			no_of_hits += 1  # += means add one to value and reassign
	return 4 * (no_of_hits / total_iterations)


def get_variance(total_iterations):
	p = pi / AREA_OF_SQUARE
	return (4 ** 2) * (p * (1-p) / total_iterations)


estimated_pi = estimate_pi(NUMBER_OF_ITERATIONS)
variance = get_variance(NUMBER_OF_ITERATIONS)
print(estimated_pi, variance)