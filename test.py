import pytest

import numpy as np

from path_finding import our_dijkstra
from a_star_algorithm import Graph


@pytest.fixture
def igor_graph():
    node_0 = [0, 3, float('inf'), float('inf'), float('inf'), 5]
    node_1 = [float('inf'), 0, 7, float('inf'), float('inf'), 10]
    node_2 = [float('inf'), float('inf'), 0, 5, 1, float('inf')]
    node_3 = [float('inf'), float('inf'), float('inf'), 0, 6, float('inf')]
    node_4 = [float('inf'), float('inf'), float('inf'), float('inf'), 0, 7]
    node_5 = [float('inf'), float('inf'), 8, 2, float('inf'), 0]

    graph = np.array([node_0, node_1, node_2,
                      node_3, node_4, node_5])

    return graph


@pytest.fixture
def bidirectional_graph():
    node_0 = [0, 4, 2, float('inf'), float('inf'), 4, float('inf')]
    node_1 = [4, 0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
    node_2 = [2, float('inf'), 0, float('inf'), 1, float('inf'), 5]
    node_3 = [float('inf'), float('inf'), float('inf'), 0, 3, 2, float('inf')]
    node_4 = [float('inf'), float('inf'), 1, 3, 0, float('inf'), float('inf')]
    node_5 = [4, float('inf'), float('inf'), 2, float('inf'), 0, float('inf')]
    node_6 = [float('inf'), float('inf'), 5, float('inf'), float('inf'), float('inf'), 0]

    graph = np.array([node_0, node_1, node_2,
                      node_3, node_4, node_5, node_6])

    return graph


def test_our_dijkstra(igor_graph, benchmark):

    benchmark(our_dijkstra, graph=igor_graph, end_node=0)

    # shortest_path, distance = our_dijkstra(igor_graph, 4)
    # print(f'Shortest Path: {shortest_path}\n')
    # print(f'Distance: {distance}')


def test_our_dijkstra_bidirectional(bidirectional_graph, benchmark):

    # for i in range(len(bidirectional_graph)):
    #     for j in range(len(bidirectional_graph)):
    #         shortest_path, distance = our_dijkstra(bidirectional_graph, end_node=j, start_node=i)
    #         print(f'Distance: {distance}')
    #         print(f'Shortest Path from {i} to {j}: {shortest_path}\n')

    benchmark(our_dijkstra, bidirectional_graph, end_node=6, start_node=0)


def test_astar(benchmark):

    adjacency_list = {
        0: [(1, 4), (2, 2), (5, 4)],
        1: [(0, 4)],
        2: [(4, 1), (6, 5)], 
        3: [(4, 3), (5, 2)],
        4: [(3, 3), (2, 1)],
        5: [(3, 2), (0, 4)],
        6: [(2, 5)]
    }

    graph1 = Graph(adjacency_list)
    
    #shortest_path, distance = graph1.a_star_algorithm(0, 4)
    #print(f'Shortest Path: {shortest_path}\n')
    #print(f'Distance: {distance}')

    benchmark(graph1.a_star_algorithm, start_node=0, stop_node=0)