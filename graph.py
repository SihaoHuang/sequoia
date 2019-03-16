#!/usr/bin/env python

import matplotlib.pyplot as plt
from networkx import nx

DG=nx.DiGraph()
DG.add_node("18.01")
DG.add_node("18.02")
DG.add_node("18.06")
DG.add_edge("18.01", "18.02") 
DG.add_edge("18.02", "18.06") 
print(DG.edges("18.01"))

# pathlengths = []

# print("source vertex {target:length, }")
# for v in G.nodes():
#     spl = dict(nx.single_source_shortest_path_length(G, v))
#     print('{} {} '.format(v, spl))
#     for p in spl:
#         pathlengths.append(spl[p])

# print('')
# print("average shortest path length %s" % (sum(pathlengths) / len(pathlengths)))

# # histogram of path lengths
# dist = {}
# for p in pathlengths:
#     if p in dist:
#         dist[p] += 1
#     else:
#         dist[p] = 1

# print('')
# print("length #paths")
# verts = dist.keys()
# for d in sorted(verts):
#     print('%s %d' % (d, dist[d]))

# print("radius: %d" % nx.radius(G))
# print("diameter: %d" % nx.diameter(G))
# print("eccentricity: %s" % nx.eccentricity(G))
# print("center: %s" % nx.center(G))
# print("periphery: %s" % nx.periphery(G))
# print("density: %s" % nx.density(G))

# #nx.draw(G, with_labels=True)
# nx.draw(G, with_labels=True)
# plt.show()
