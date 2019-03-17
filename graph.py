#!/usr/bin/env python

import matplotlib.pyplot as plt
from networkx import nx
from load_data import CourseData

course_data = CourseData("edited_course.json")

DG=nx.DiGraph()

course_dict = course_data.create_course_dict()
course_list = course_data.get_course_list()

# course_dict = {"1.00": {"type":"Class", "id":"21M.714", "label":"Contemporary American Theater", "shortLabel":"Contemporary American Theater", "level":"Undergraduate", "hi":"", "total_units":12, "units":"3_0_9", "course":"21M", "description":"Examines the exciting terrain of contemporary American writing for the theater, focusing on what is known in New York as \"Off Broadway,\" \"downtown,\" or \"indie theater.\" Students read work by influential playwrights from earlier generations alongside plays by new voices currently in production in Boston, New York, and across the country. Students also examine the changing institution of American theater, reading a selection of plays in order to determine what constellation of issues and concerns they engage. Discussions unpack how these plays reflect, challenge and re_construct the idea of America in the 21st century. Enrollment limited.", "prereqs":"", "offering":"Y", "semester":["Spring"], "in_charge":"Urban, Kenneth", "year":"2019", "master_subject_id":"21M.714", "equivalent_subjects":[""], "joint_subjects":[""], "meets_with_subjects":[""], "fall_instructors":["K. Urban"], "spring_instructors":["K. Urban"], "is_variable_units":"N", "hass_attribute":"HA", "comm_req_attribute":"CIH", "gir_attribute":""}}
# course_list = ["1.00"]

for node in course_list:
    DG.add_node(node)
    attribute_dict = course_dict[node]
    for key in attribute_dict:
        DG.node[node][key] = attribute_dict[key]
    prereq_string = DG.node[node]["prereqs"]
    prereqs = course_data.create_prereq_list(prereq_string)
    for prereq in prereqs:
        DG.add_edge(prereq, node)


pos = nx.kamada_kawai_layout(DG)


# test nodes:
# DG=nx.DiGraph()
# DG.add_node("18.01")
# DG.add_node("18.02")
# DG.add_node("18.06")
# DG.add_edge("18.01", "18.02") 
# DG.add_edge("18.02", "18.03") 
# DG.add_edge("18.02", "18.06") 


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



plt.figure(3,figsize=(13,7)) 
nx.draw_networkx_nodes(DG, with_labels=True, node_size = 80)
plt.show()

# print(DG.nodes())
# print(len(DG.nodes()))
