#!/usr/bin/env python

import matplotlib.pyplot as plt
from networkx import nx
from load_data import CourseData

course_data = CourseData("course_data.json")

DG=nx.DiGraph()

course_dict = course_data.create_course_dict()

for node in course_data.get_course_list():
    DG.add_node(node)
    attribute_dict = course_dict[node]
    for key in attribute_dict:
        DG.node[node][key] = attribute_dict[key]


# test nodes:
# test_DG=nx.DiGraph()
# test_DG.add_node("18.01")
# test_DG.add_node("18.02")
# test_DG.add_node("18.06")
# test_DG.add_edge("18.01", "18.02") 
# test_DG.add_edge("18.02", "18.03") 
# test_DG.add_edge("18.02", "18.06") 


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

pos = nx.shell_layout(DG)

plt.figure(3,figsize=(13,7)) 
nx.draw_networkx(DG, with_labels=False, node_size = 80)
plt.show()

# print(DG.nodes())
# print(len(DG.nodes()))