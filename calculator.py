from __future__ import division

from math import exp, pi, sqrt

from constants import Q, R, a


def summation_function(x, wx):
    return pow(x, 2) / (exp(-x) + exp(-R/a)) * wx


def summation(data_series):
    result = 0
    for x, wx in data_series:
        result += summation_function(x, wx)
    return result


def find_C_for(data_series):
    multiplier = Q / (4 * pi * pow(a, 3))
    return multiplier * pow(summation(data_series), -1)


def find_Q_for(data_series, m):
    multiplier = 4 * pi * pow(a, 3 + m)
    C = find_C_for(data_series)
    return multiplier * C * summation(data_series)


def find_rms_for(data_series):
    return sqrt(
        pow(a, 2) * find_Q_for(data_series, 2) / find_Q_for(data_series, 0)
    )
