#!/usr/bin/env python

from calculator import find_C_for
from data import DataSet


def main():
    ds = DataSet()
    for node in ds.nodes:
        print(find_C_for(node.data_tuples))


if __name__ == '__main__':
    main()
