import random

## Vertex cover
#  Find the set of vertices to cover all edges
#  Implement vertex cover with undirected and unweighted graph

class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.adj[node2]:
            self.adj[node2].remove(node1)
            self.adj[node1].remove(node2)

    def remove_incident_edges(self, node):
        for neighbour in self.adj[node]:
            self.adj[neighbour].remove(node)
        self.adj[node] = []

    def are_connected(self, node1, node2):
        for node in adj[node1]:
            if node == node2:
                return True
        return False

    def adj_nodes(self, node):
        return self.adj[node]

    def has_no_edges(self):
        for node in self.adj:
            if len(self.adj[node]) > 0:
                return False
        return True

    def copy(self):
        new_G = Graph()
        new_G.adj = self.adj.copy()
        for node in self.adj:
            new_G.adj[node] = self.adj[node].copy()
        return new_G

    def number_of_nodes(self):
        return len(self.adj)


## Vertex cover
def vertex_cover(G):
    vc = list(G.adj.keys())
    nodes = power_set(vc)
    for node in nodes:
        cg = G.copy()
        for elem in node:
            cg.remove_incident_edges(elem)
        if cg.has_no_edges() and len(node) < len(vc):
            vc = node
    return vc


# powerset
# is empty
def is_vertex_cover(G, cover):                  # if is_vertex_cover(G, [0])
    temp_G = G.copy()                           # temp_G = {0:[1,2,3], 1:[0,2], 2:[0,1], 3:[0]}
    for node in cover:
        temp_G.remove_incident_edges(node)      # temp_G.remove_incident_edges(0)
    if temp_G.has_no_edges():                   # if temp_G.has_no_edges() true means, "cover" is a vertex_cover 
        return True
    return False

def power_set(elements):
    if elements == []:
        return [[]]
    return add_to_each(power_set(elements[1:]), elements[0]) + power_set(elements[1:])


def add_to_each(sets, element):
    my_sets = sets.copy()
    for my_set in my_sets:
        my_set.append(element)
    return my_sets

graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

vc = vertex_cover(graph)
print(vc)