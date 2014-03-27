import LT.box as B
import numpy as np
import matplotlib as mpl

#get data
datafile = B.get_file('gauss_laguerre_modified.data')
nodes = B.get_data(datafile, 'node')
xvalues = B.get_data(datafile, 'x')
weights = B.get_data(datafile, 'weight')

#put data into useable form
node_lookup = {} #creates an empty dictionary
for node, xvalues, weight in zip(nodes, xvalues, weights): #loops through each node, zip creates list of tuples
    node_pairs = node_lookup.setdefault(node, [])
    node_pairs.append((xvalues, weight))

for node, node_pairs in node_lookup.items(): # "items" must modify a dictionary
    for pair in node_pairs:
        print('{} {} {}'.format(node, *pair))
