import re

from calculator import find_C_for, find_Q_for, find_rms_for
from constants import DATA_SOURCE_FP


def parse_data(line):
    re_node_data = re.compile('^\s+(\d+\.\d+E[+-]\d+)\s+(\d+\.\d+E[+-]\d+)')
    return re_node_data.match(line).groups()


def parse_file(fp):
    re_node_marker = re.compile('^\s+\d+\s*$')
    node_data = []
    with open(fp) as of:
        next(of)  # Skip the first line
        for line in of:
            if re_node_marker.match(line):
                yield node_data
                node_data = []
                continue
            node_data.append(parse_data(line))
    yield node_data


class DataSet(object):
    @property
    def nodes(self):
        _nodes = []
        for node_data in parse_file(DATA_SOURCE_FP):
            _nodes.append(Node(node_data))
        return _nodes


class Node(object):
    def __init__(self, data_tuples):
        self.data_tuples = map(tuple, (map(float, t) for t in data_tuples))

    @property
    def C(self):
        return find_C_for(self.data_tuples)

    def Q(self, m):
        return find_Q_for(self.data_tuples, m)

    @property
    def rms(self):
        return find_rms_for(self.data_tuples, self.Q(2), self.Q(0))
