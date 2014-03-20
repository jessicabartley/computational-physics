import re

from calculator import find_C_for, find_rms_for, summation
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
    def __init__(self):
        self._nodes = []

    @property
    def nodes(self):
        if self._nodes:
            return self._nodes
        for node_data in parse_file(DATA_SOURCE_FP):
            self._nodes.append(Node(node_data, self))
        return self._nodes

    @property
    def C(self):
        return self.nodes[-1].C


class Node(object):
    def __init__(self, data_tuples, dataset):
        self.data_tuples = map(tuple, (map(float, t) for t in data_tuples))
        self.dataset = dataset

    def sum(self, m):
        return summation(self.data_tuples, m)

    @property
    def C(self):
        return find_C_for(self.data_tuples)

    @property
    def rms(self):
        return find_rms_for(self.data_tuples, self.sum(2), self.sum(0))
