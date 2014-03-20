from __future__ import division

from math import exp, pi, sqrt

import constants


def summation_function(x, wx, m):
    return pow(x, 2 + m) / (exp(-x) + exp(-constants.R/constants.a)) * wx


def summation(data_series, m):
    result = 0
    for x, wx in data_series:
        result += summation_function(x, wx, m)
    return result


def find_C_for(data_series):
    multiplier = constants.Q / (4 * pi * pow(constants.a, 3))
    return multiplier * pow(summation(data_series, 0), -1)


def find_rms_for(data_series, numerator, denominator):
    return sqrt(pow(constants.a, 2) * numerator / denominator)
