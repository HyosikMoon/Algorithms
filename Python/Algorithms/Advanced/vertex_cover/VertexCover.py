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

    def remove_incident_edge(self, node):
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

    def has_no_edges(self, node):
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