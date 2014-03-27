#!/usr/bin/env python
from __future__ import division

from math import pi, sqrt
from random import random

# For this project we're assuming the sphere has a radius of 1

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
        # `*coordinates` expands the coordinates iterable (could be a tuple or
        # list), and pass the individual elements as arguments to the
        # `find_length()` function
        length = find_length(*coordinates)
        if is_within_circle(length):
            # `+=` adds 1 to the variable (`no_of_hits` in this case) and
            # updates the variable to the new value at the same time. It's a
            # shorthand for `no_of_hits = no_of_hits + 1`
            no_of_hits += 1
    return 4 * (no_of_hits / total_iterations)


def get_variance(total_iterations):
    p = pi / AREA_OF_SQUARE
    return (4 ** 2) * (p * (1-p) / total_iterations)


estimated_pi = estimate_pi(NUMBER_OF_ITERATIONS)
variance = get_variance(NUMBER_OF_ITERATIONS)
print(estimated_pi, variance)
