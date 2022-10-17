import numpy as np


dist = np.array([[0, 5, 0, 6, 0, 4, 0, 7], [5, 0, 2, 4, 3, 0, 0, 0], [0, 2, 0, 1, 0, 0, 0, 0], [6, 4, 1, 0, 7, 0, 0, 0], [0, 3, 0, 7, 0, 0, 6, 4], [4, 0, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 6, 3, 0, 2], [7, 0, 0, 0, 4, 0, 2, 0]])

def cal_dist(distance, nodes):
    d = 0
    for i in range(len(nodes)):
        d = d + distance[nodes[i % 8], nodes[(i + 1) % 8]]
    return d

nodes = np.array([0, 1, 2, 3, 4, 5, 6, 7])
dist_final = []

for i in range(50):
    a = np.random.randint(1, 8 - 1)
    d = cal_dist(dist, nodes)
    dist_final.append(d)

    nodes[[a, (a + 1) % 8]] = nodes[[(a + 1) % 8, a]]

print (cal_dist(dist, nodes))