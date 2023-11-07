import numpy as np


def dijkstra(graph: np.array):
    # Some variables to keep track of:

    visited_nodes = []
    unvisited_nodes = list(range(len(graph)))

    cur_node = 0
    unvisited_nodes.remove(cur_node)
    visited_nodes.append(cur_node)
    # Make shallow copy of distances from current node
    d_i = graph[cur_node].copy()

    # Keep track of nodes resulting in the shortest path
    node_paths = {}
    for node in range(len(graph)):
        node_paths[node] = [0]

    while len(visited_nodes) < len(graph):
        distances = d_i.copy()
        # Replace distance to visited nodes with infinity temporarily so that they can't be visited again
        for node in visited_nodes:
            distances[node] = float('inf')
        # Identify current node from set of unvisited nodes that has minimum distance from previous
        cur_node = np.where(distances == min(distances))[0][0]
        # Distance from previous node to current node
        dc = distances[cur_node]
        # Distance from prev to c to all other nodes
        d_i_sum = dc + graph[cur_node]
        # Take minimum distance from cur_node to all other nodes
        for d in range(len(d_i_sum)):
            if d_i_sum[d] < d_i[d]:
                if cur_node not in node_paths[d]: node_paths[d].append(cur_node)
            elif d_i_sum[d] > d_i[d]:
                if d not in node_paths[d]: node_paths[d].append(d)
        d_i = np.minimum(d_i, d_i_sum)

        visited_nodes.append(cur_node)
        unvisited_nodes.remove(cur_node)

    print(d_i)
    print(node_paths)





