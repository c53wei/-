import pytest

import numpy as np

from path_finding import our_dijkstra
from astaralgorithm import Graph

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

    shortest_path, distance = our_dijkstra(igor_graph, 4)
    print(f'Shortest Path: {shortest_path}\n')
    print(f'Distance: {distance}')

def test_astar(benchmark):


    # TEST CASE 1
    adjacency_list = {
        0: [(1, 3), (5, 5)],
        1: [(5, 10), (2, 7)],
        2: [(3, 4), (4, 1)], 
        3: [(4, 6)],
        4: [(5, 7)],
        5: [(3, 2), (2, 8)]
    }


    '''
    # TEST CASE 2
    adjacency_list = {
        0: [(1, 5), (2, 15)],
        1: [(2, 6), (3, 4)],
        2: [(4, 2)],
        3: [(4, 3)]
    }
    '''


    graph1 = Graph(adjacency_list)
    shortest_path, distance = graph1.a_star_algorithm(0, 4)

    # benchmark(graph1.a_star_algorithm, start_node=0, stop_node=4)

    print(f'Shortest Path: {shortest_path}\n')
    print(f'Distance: {distance}')