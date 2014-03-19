from __future__ import division

from math import exp, pi, sqrt

import constants


def summation_function(x, wx):
    return pow(x, 2) / (exp(-x) + exp(-constants.R/constants.a)) * wx


def summation(data_series):
    result = 0
    for x, wx in data_series:
        result += summation_function(x, wx)
    return result


def find_C_for(data_series):
    multiplier = constants.Q / (4 * pi * pow(constants.a, 3))
    return multiplier * pow(summation(data_series), -1)


def find_Q_for(data_series, m, C):
    multiplier = 4 * pi * pow(constants.a, 3 + m)
    return multiplier * C * summation(data_series)


def find_rms_for(data_series, numerator, denominator):
    return sqrt(pow(constants.a, 2) * numerator / denominator)
