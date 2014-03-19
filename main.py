#!/usr/bin/env python

from collections import OrderedDict

from data import DataSet
import constants

WIDTH = 10
SPACER = '  '

COLUMNS = OrderedDict([
    ('node', dict(align='^', width=4, format='')),
    ('sum', dict(align='^', width=WIDTH, format='.6f')),
    ('C', dict(align='^', width=WIDTH, format='.8f')),
    ('Q(2)', dict(align='^', width=WIDTH, format='.8f')),
    ('Q(0)', dict(align='^', width=WIDTH, format='.7f')),
    ('Q(2)/Q(0)', dict(align='^', width=WIDTH, format='.8f')),
    ('rms', dict(align='^', width=WIDTH, format='.8f')),
])


def column_widths():
    return (v['width'] for v in COLUMNS.values())


def main():
    ds = DataSet()
    print('Constants:')
    print('            A = {}'.format(constants.A))
    print('            Q = {}'.format(constants.Q))
    print('            R = {}'.format(constants.R))
    print('            a = {}'.format(constants.a))
    print('  Converged C = {}'.format(ds.C))
    print

    _str = SPACER.join(
        '{{:{align}{width}}}'.format(**v) for v in COLUMNS.values()
    )
    print(_str.format(*COLUMNS.keys()))
    print(SPACER.join(['-' * w for w in column_widths()]))

    for i, node in enumerate(ds.nodes, start=1):
        _str = SPACER.join(
            '{{:>{width}{format}}}'.format(**v) for v in COLUMNS.values()
        )
        output = _str.format(
            i, node.sum, node.C, node.Q(2), node.Q(0), node.Q(2) / node.Q(0),
            node.rms
        )
        print(output)


if __name__ == '__main__':
    main()
