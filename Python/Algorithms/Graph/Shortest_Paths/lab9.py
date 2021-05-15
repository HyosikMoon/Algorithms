import random
import timeit
import matplotlib.pyplot as plt
import min_heap
import Bellman_Ford
import Dijkstra

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node2]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist[node] = 99999
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its node as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[999999 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i,j):
                d[i][j] = G.w(i,j)
        d[i][i] = 0
    return d


## Test ##
## Case0
# G = DirectedWeightedGraph()
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")

# G.add_edge("A","B",10)
# G.add_edge("B","C",10)
# G.add_edge("A","C",30)

# ## Case1
# G = DirectedWeightedGraph()
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")

# G.add_edge("A","C",20)
# G.add_edge("A","D",15)
# G.add_edge("A","B",60)
# G.add_edge("C","B",5)
# G.add_edge("C","D",30)
# G.add_edge("B","D",10)

## Case2
# G = DirectedWeightedGraph()
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")
# G.add_node("E")
# G.add_node("F")

# G.add_edge("A","B",2)
# G.add_edge("A","C",4)
# G.add_edge("C","E",3)
# G.add_edge("B","C",1)
# G.add_edge("B","D",4)
# G.add_edge("B","E",2)
# G.add_edge("E","D",3)
# G.add_edge("D","F",2)
# G.add_edge("E","F",2)

# print(G.adj)
# print(G.weights)

# dij = dijkstra(G, "A")
# bell = bellman_ford(G, "A")

# print(dij)
# print(dij)


## Case3
# G = create_random_complete_graph(5,10)
# G = DirectedWeightedGraph()
# G.add_node(0)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# G.add_edge(0,1,40)
# G.add_edge(0,2,10)
# G.add_edge(1,3,50)
# G.add_edge(0,3,60)
# G.add_edge(1,2,20)
# G.add_edge(2,3,30)
# m = mystery(G)


## Case4
G = DirectedWeightedGraph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

G.add_edge("A","C",20)
G.add_edge("A","D",15)
G.add_edge("A","B",60)
G.add_edge("C","B",5)
G.add_edge("C","D",30)
G.add_edge("B","D",10)

print(G.adj)
print(G.weights)

bell = Bellman_Ford.bellman_ford(G, "A")
bell_apro = Bellman_Ford.bellman_ford_approx(G, "A", 2)

print(bell)
print(bell_apro)

dij = dijkstra(G, "A")
print(dij)

################## Time teest ##################
# G = create_random_complete_graph(100,1000)
# k = []
# dist = []
# runtime = []

# for i in range(1, 101):
#     start_f1 = timeit.default_timer()
#     dist_i = sol9.bellman_ford_approx(G, 0, i)
#     end_f1 = timeit.default_timer()

#     k.append(i)
#     runtime.append(end_f1 - start_f1)
#     dist.append(total_dist(dist_i))

# plt.scatter(k, runtime, marker='.', label = "Runtime")
# # plt.scatter(k, dist, marker='.', label = "Distance")
# plt.xlabel("k")
# plt.ylabel("Runtime, Distance")
# plt.legend(loc='upper left')
# plt.show()
# plt.savefig("./Figures/" + "Bellman_Ford_approx_distance")
# plt.close()


################## All Pairs Shortest Paths ##################
# G = create_random_complete_graph(10,100)
# bellford = bellman_ford(G,0)
# distance = total_dist(bellford)

# all_pairs_dist = 0
# myst = mystery(G)

# print(myst.dist)

# for i in range(len(myst[0])):
#     all_pairs_dist += myst[0][i]

# print("distance: " , distance, type(distance))
# print("all_pairs_dist: " , all_pairs_dist)