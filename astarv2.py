from queue import PriorityQueue
path = []
explored = []
visited = {}
distance = 0


class Graph:

    def __init__(self, directed=False):
        self._outgoing = {}
        # If the graph is undirected, 'self._outgoing'
        # is the universal storage.
        self._incoming = {} if directed else self._outgoing

    # If the graph is directed, the 'self._incoming' 
    # dictionary differs from the 'self._outgoing'.
    def is_directed(self):
        return self._incoming is not self._outgoing

    # The function returns a generator of incoming
    # or outgoing (default) edges of a vertex.
    def adjacent_edges(self, vertex, outgoing=True):
        # References the corresponding outer dictionary
        # (dictionary of dictionaries)
        adj_edges = self._outgoing if outgoing else self._incoming

        # Access each of the edges for this endpoint vertex.
        for edge in adj_edges[vertex].values():
            yield edge

    def add_vertex(self, entity=None, h=None, cost=None):
        # Constructs a new vertex from the entity.
        vertex = self.Vertex(entity, h, cost)
        # The vertex becomes a key in the outer dictionary,
        # but the value is an internal dictionary (as we model
        # both dimensions for each edge: origin and destination).
        # e.g. {vertex_1a:{vertex_b:edge_a_b}, vertex_b:{vertex_c:edge_b_c}}.
        self._outgoing[vertex] = {}
        if self.is_directed():
            self._incoming[vertex] = {}

    def add_edge(self, origin, destination, weight=None):
        # Constructs a new edge from the vertices.
        edge = self.Edge(origin, destination, weight)
        # Adds the edge to the dictionary (dictionaries are
        # the same if the graph is undirected). The outer key
        # represents the origin, i.e. the component 'a' of
        # the edge-defining pair (a, b). The inner key stands
        # for the component 'b' of the edge-defining pair (a, b).
        self._outgoing[origin][destination] = edge
        # Even if the graph is undirected, each edge has to
        # be added twice, i.e. once for each of its endpoints.
        self._incoming[destination][origin] = edge

    def vertices(self):
        return self._outgoing.keys()

    def edges(self):
        # All the edges are collected into a set.
        result = set()
        for inner_dict in self._outgoing.values():
            result.update(inner_dict.values())
        return result

    class Vertex:
        __slots__ = '_entity', '_h', '_cost'

        def __init__(self, entity, h=None, cost=None):
            self.entity = entity
            self.h = h
            self.cost = cost

        # The real-world entity is represented by the Vertex object.
        @property
        def entity(self):
            return self._entity

        @entity.setter
        def entity(self, entity):
            self._entity = entity

        # The real-world entity has a heuristic value of 'h'.
        @property
        def h(self):
            return self._h

        @h.setter
        def h(self, h):
            self._h = h

        # The real-world entity has a cost of 'cost'.
        @property
        def cost(self):
            return self._cost

        @cost.setter
        def cost(self, cost):
            self._cost = cost

        # We have to implement __hash__ to use the object as a dictionary key.
        def __hash__(self):
            return hash(id(self))

        def __lt__(self, other):
            if self.cost is None:
                return False
            elif other.cost is None:
                return True
            else:
                return self.cost < other.cost

    class Edge:
        __slots__ = '_origin', '_destination', '_weight'

        def __init__(self, origin, destination, weight=None):
            self._origin = origin
            self._destination = destination
            self.weight = weight

        def endpoints(self):
            return self._origin, self._destination

        # Returns the other component of the edge-defining pair (a, b)
        # for a given component a or b, respectively.
        def opposite(self, vertex):
            return self._destination if self._origin is vertex \
                else self._origin

        # Returns the weight of the edge.
        @property
        def weight(self):
            return self._weight

        # Sets the weight of the edge
        @weight.setter
        def weight(self, weight):
            self._weight = weight

        def __hash__(self):
            return hash((self._origin, self._destination))

def a_star(graph, start_vertex, target):
    # Create the priority queue for open vertices.
    vertices_pq = PriorityQueue()

    start_vertex.cost = start_vertex.h

    # Adds the start vertex to the priority queue.
    #print(f'Visiting/queueing vertex {start_vertex.entity}')
    vertices_pq.put(start_vertex)

    # The starting vertex is visited first and has no leading edges.
    # If we did not put it into 'visited' in the first iteration,
    # it would end up in 'visited' during the second iteration, pointed to
    # by one of its children vertices as a previously unvisited vertex.
    visited[start_vertex] = None

    # Loops until the priority list gets empty.
    while not vertices_pq.empty():
        # Gets the vertex with the lowest cost.
        vertex = vertices_pq.get()
        # If the vertex being explored is a target vertex, ends the algorithm.
        #print(f'Exploring vertex {vertex.entity}')
        if vertex.entity == target:
            return vertex
        # Examines each non-visited adjoining edge/vertex.
        for edge in graph.adjacent_edges(vertex):
            # Gets the second endpoint.
            v_2nd_endpoint = edge.opposite(vertex)

            # Skips the explored vertices.
            if v_2nd_endpoint in explored:
                continue

            # Checks if the endpoint has a weight and is the weight the cheapest one.
            if v_2nd_endpoint.cost is None \
                    or vertex.cost - vertex.h + edge.weight < v_2nd_endpoint.cost - v_2nd_endpoint.h:
                # Adds the second endpoint to 'visited' and maps
                # the leading edge for the search path reconstruction.
                v_2nd_endpoint.cost = vertex.cost - vertex.h + edge.weight + v_2nd_endpoint.h
                # Prevents reinsertion to the priority queue. The
                # endpoint distance value will be updated.
                if v_2nd_endpoint not in visited:
                    #print(f'Visiting/queueing vertex {v_2nd_endpoint.entity}')
                    vertices_pq.put(v_2nd_endpoint)
                # Forces the priority queue to recalculate in case of an
                # inner vertex update resulting with the highest priority
                vertices_pq.put(vertices_pq.get())
                # Replaces the previous vertex' ancestor with a cheaper one.
                visited[v_2nd_endpoint] = edge
        # The vertex is used for update and put aside.
        explored.append(vertex)
    return None


def convertresult(result):
    if result is not None:
    # The search path ends with the found vertex (entity).
    # Each vertex is a container for its real-world entity.
        path_vertex = result
    # The entity is added to the 'path'.
        path.append(path_vertex.entity)
    # Constructs the rest of the search path (if it exists)...
        while True:
        # Gets a discovery edge leading to the vertex.
            path_edge = visited.get(path_vertex)
        # If the path vertex is the root, it has no discovery edge...
            if path_edge is None:
                break
        # Otherwise, gets the second (parent vertex) endpoint.
            path_vertex = path_edge.opposite(path_vertex)
        # The entity is added to the 'path'.
            path.append(path_vertex.entity)
    # The path is reversed and starts with the root vertex.
        return (path[::-1])
    else:
        print('\nEntity is not found')

