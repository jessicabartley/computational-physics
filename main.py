#!/usr/bin/env python

from calculator import find_C_for, find_rms_for
from data import DataSet


def main():
    ds = DataSet()
    for i, node in enumerate(ds.nodes, start=1):
        C = find_C_for(node.data_tuples)
        rms = find_rms_for(node.data_tuples)
        print('Node {}: C={}, rms={}'.format(i, C, rms))


if __name__ == '__main__':
    main()
