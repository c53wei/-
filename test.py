import pytest

import numpy as np

from path_finding import our_dijkstra
from astaralgorithm import Graph
from astarv2 import a_star, Graph, convertresult


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


def test_astarv2(benchmark):
    g = Graph()
    # Loads the graph with the first seven vertices.
    g.add_vertex(0, 4)
    g.add_vertex(1, 4)
    g.add_vertex(2, 2)
    g.add_vertex(3, 7)
    g.add_vertex(4, 5)
    g.add_vertex(5, 10)
    g.add_vertex(6, 0)
    # Constructs the 'vertices' dictionary for a more
    # convenient access during the graph construction.
    vertices = {k.entity: k for k in g.vertices()}
    # Constructs an arbitrary graph from
    # the existing vertices and edges.
    g.add_edge(vertices[0], vertices[1], 4)
    g.add_edge(vertices[0], vertices[2], 2)
    g.add_edge(vertices[2], vertices[4], 1)
    g.add_edge(vertices[4], vertices[3], 3)
    g.add_edge(vertices[3], vertices[5], 2)
    g.add_edge(vertices[0], vertices[5], 4)
    g.add_edge(vertices[2], vertices[6], 5)

    #result = a_star(g, vertices[0], 0)
    #shortest_path = convertresult(result)
    #print(f'Shortest Path: {shortest_path}\n')

    benchmark(a_star, g, vertices[0], 6)
