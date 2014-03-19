from __future__ import division

from math import exp, pi

from constants import Q, R, a


def summation_function(x, wx):
    return pow(x, 2) / (exp(-x) + exp(-R/a)) * wx


def summation(data_series):
    result = 0
    for x, wx in data_series:
        result += summation_function(x, wx)
    return result


def find_C_for(data_series):
    constant = Q / (4 * pi * pow(a, 3))
    return constant * pow(summation(data_series), -1)
