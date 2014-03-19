from __future__ import division

import os

A = 40  # Atomic Mass
Q = 20  # Atomic Number
R = 1.1 * pow(A, 1/3)
a = 0.55  # in fm

DATA_SOURCE_FP = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'gauss_laguerre.dat')
)
