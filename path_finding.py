import numpy as np


def our_dijkstra(graph: np.array, end_node: int, start_node: int = 0):
    # Some variables to keep track of:

    visited_nodes = []
    unvisited_nodes = list(range(len(graph)))

    cur_node = start_node
    unvisited_nodes.remove(cur_node)
    visited_nodes.append(cur_node)
    # Make shallow copy of distances from current node
    d_i = graph[cur_node].copy()
    prev_d_i = [float('inf')]*len(d_i)

    # Keep track of nodes resulting in the shortest path
    node_paths = {}
    for node in range(len(graph)):
        node_paths[node] = [start_node]

    while len(visited_nodes) < len(graph):
        # Update new shortest paths
        for i, dist in enumerate(d_i):
            if dist < prev_d_i[i]:
                if i not in node_paths[i]:
                    node_paths[i] = node_paths[cur_node] + [i]

        distances = d_i.copy()
        # Replace distance to visited nodes with infinity temporarily so that they can't be visited again
        for node in visited_nodes:
            distances[node] = float('inf')
        # Identify current node from set of unvisited nodes that has minimum distance from previous
        cur_node = np.where(distances == min(distances))[0][0]
        # Distance from previous node to current node
        d_c = distances[cur_node]
        # Distance from prev to c to all other nodes
        d_i_sum = d_c + graph[cur_node]
        # Take minimum distance from cur_node to all other nodes
        prev_d_i = d_i.copy()
        d_i = np.minimum(d_i, d_i_sum)

        visited_nodes.append(cur_node)
        unvisited_nodes.remove(cur_node)

    return node_paths[end_node], d_i[end_node]





