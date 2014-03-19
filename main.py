#!/usr/bin/env python

from data import DataSet


def main():
    ds = DataSet()
    for i, node in enumerate(ds.nodes, start=1):
        print('Node {}: C={}, rms={}'.format(i, node.C, node.rms))


if __name__ == '__main__':
    main()
