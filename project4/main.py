#!/usr/bin/env python
from __future__ import division

from math import pi, sqrt, gamma
from random import random
from string import lowercase

# For this project we're assuming the sphere has a radius of 1

NUMBER_OF_DIMENSIONS = 12
NUMBER_OF_ITERATIONS = 50000


def area_of_square(no_dimensions):
    area_square = 2 ** no_dimensions
    return area_square


def area_of_sphere(no_dimensions):
    area_sphere = (pi ** (NUMBER_OF_DIMENSIONS / 2)) / (gamma(NUMBER_OF_DIMENSIONS / 2 +1))
    return area_sphere


def generate_coordinates(no_dimensions):
    coordinates = []
    for i in range(no_dimensions):
        coordinates.append(2 * random() - 1)
    return coordinates


def find_length(coordinates):
    sum_of_squares = 0
    for i in range(NUMBER_OF_DIMENSIONS):
        sum_of_squares += coordinates[i] ** 2
    length = sqrt(sum_of_squares)
    return length


def is_within_circle(length):
    return length <= 1


def estimate_pi(total_iterations):
    no_of_hits = 0
    for i in xrange(total_iterations):
        coordinates = generate_coordinates(NUMBER_OF_DIMENSIONS)  # 2 dimensions only
        # `*coordinates` expands the coordinates (could be a tuple or
        # list), and pass the individual elements as arguments to the
        # `find_length()` function
        length = find_length(coordinates)
        if is_within_circle(length):
            # `+=` adds 1 to the variable (`no_of_hits` in this case) and
            # updates the variable to the new value at the same time. It's a
            # shorthand for `no_of_hits = no_of_hits + 1`
            no_of_hits += 1
    return 4 * ((no_of_hits / total_iterations) * (gamma(NUMBER_OF_DIMENSIONS / 2 +1))) ** (2 / NUMBER_OF_DIMENSIONS)


def get_variance(total_iterations):
    p = area_of_sphere(NUMBER_OF_DIMENSIONS) / area_of_square(NUMBER_OF_DIMENSIONS)
    variance = (4. ** 2.) * (p * (1-p) / total_iterations)
    return variance


def get_error(total_iterations):
    variance = get_variance(total_iterations)
    return sqrt(variance)


estimated_pi = estimate_pi(NUMBER_OF_ITERATIONS)
sigma = get_error(NUMBER_OF_ITERATIONS)
print NUMBER_OF_DIMENSIONS, estimated_pi, sigma
