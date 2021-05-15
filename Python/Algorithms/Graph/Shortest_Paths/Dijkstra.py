import min_heap

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


## Case1
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

# dij = dijkstra(G, "A")