from LT import box as B

f = B.get_file('gauss_laguerre_modified.data')
nodes = B.get_data(f, 'node')
xs = B.get_data(f, 'x')
weights = B.get_data(f, 'weight')

node_lookup = {}
for node, x, weight in zip(nodes, xs, weights):
    import pdb
    pdb.set_trace()
    node_pairs = node_lookup.setdefault(node, [])
    node_pairs.append((x, weight))

for node, node_pairs in node_lookup.items():
    for pair in node_pairs:
        print('{} {} {}'.format(node, *pair))
