import min_heap

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

def bellman_ford_approx(G, source, k):
    pred = {}
    dist = {} 
    updates = {}
    nodes = list(G.adj.keys())
    for node in nodes:
        dist[node] = 99999
        updates[node] = k
    dist[source] = 0
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if updates[neighbour] > 0:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        updates[neighbour] = updates[neighbour] - 1
                        pred[neighbour] = node
    return dist


# ## Case1
# G = lab9.DirectedWeightedGraph()
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

# print(G.adj)
# print(G.weights)

# bell = bellman_ford(G, "A")
# bell_apro = bellman_ford_approx(G, "A", 2)