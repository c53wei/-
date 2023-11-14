import pytest

import numpy as np

from path_finding import our_dijkstra


@pytest.fixture
def igor_graph():
    node_1 = [0, 3, float('inf'), float('inf'), float('inf'), 5]
    node_2 = [float('inf'), 0, 7, float('inf'), float('inf'), 10]
    node_3 = [float('inf'), float('inf'), 0, 5, 1, float('inf')]
    node_4 = [float('inf'), float('inf'), float('inf'), 0, 6, float('inf')]
    node_5 = [float('inf'), float('inf'), float('inf'), float('inf'), 0, 7]
    node_6 = [float('inf'), float('inf'), 8, 2, float('inf'), 0]

    graph = np.array([node_1, node_2, node_3,
                      node_4, node_5, node_6])

    return graph


def test_our_dijkstra(igor_graph):

    # benchmark(our_dijkstra, graph=igor_graph, end_node=0)

    shortest_path, distance = our_dijkstra(igor_graph, 2)
    print(f'Shortest Path: {shortest_path}\n')
    print(f'Distance: {distance}')
