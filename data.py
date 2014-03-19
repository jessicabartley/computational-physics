import os
import re


def parse_data(line):
    re_node_data = re.compile('^\s+(\d+\.\d+E[+-]\d+)\s+(\d+\.\d+E[+-]\d+)')
    return re_node_data.match(line).groups()


def parse_file(fp):
    re_node_marker = re.compile('^\s+\d+\s*$')
    node_data = []
    with open(fp) as of:
        next(of)
        for line in of:
            if re_node_marker.match(line):
                yield node_data
                node_data = []
                continue
            node_data.append(parse_data(line))
    yield node_data


class DataSet(object):
    def __init__(self, fp=None):
        self._nodes = []
        if not fp:
            fp = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), 'data', 'gauss_laguerre.dat'
                )
            )
        self.fp = fp

    @property
    def nodes(self):
        if self._nodes:
            return self._nodes
        for node_data in parse_file(self.fp):
            self._nodes.append(Node(node_data))
        return self._nodes


class Node(object):
    def __init__(self, data_tuples):
        self.data_tuples = map(tuple, (map(float, t) for t in data_tuples))
