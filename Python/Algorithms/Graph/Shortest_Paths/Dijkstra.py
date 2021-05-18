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


######## Geeksforgeeks.org codes #########
# # Python program for Dijkstra's single
# # source shortest path algorithm. The program is
# # for adjacency matrix representation of the graph

# # Library for INT_MAX
# import sys

# class Graph():

# 	def __init__(self, vertices):
# 		self.V = vertices
# 		self.graph = [[0 for column in range(vertices)]
# 					for row in range(vertices)]

# 	def printSolution(self, dist):
# 		print("Vertex tDistance from Source")
# 		for node in range(self.V):
# 			print(node, "t", dist[node])

# 	# A utility function to find the vertex with
# 	# minimum distance value, from the set of vertices
# 	# not yet included in shortest path tree
# 	def minDistance(self, dist, sptSet):

# 		# Initilaize minimum distance for next node
# 		min = sys.maxsize

# 		# Search not nearest vertex not in the
# 		# shortest path tree
# 		for v in range(self.V):
# 			if dist[v] < min and sptSet[v] == False:
# 				min = dist[v]
# 				min_index = v

# 		return min_index

# 	# Funtion that implements Dijkstra's single source
# 	# shortest path algorithm for a graph represented
# 	# using adjacency matrix representation
# 	def dijkstra(self, src):

# 		dist = [sys.maxsize] * self.V
# 		dist[src] = 0
# 		sptSet = [False] * self.V

# 		for cout in range(self.V):

# 			# Pick the minimum distance vertex from
# 			# the set of vertices not yet processed.
# 			# u is always equal to src in first iteration
# 			u = self.minDistance(dist, sptSet)

# 			# Put the minimum distance vertex in the
# 			# shotest path tree
# 			sptSet[u] = True

# 			# Update dist value of the adjacent vertices
# 			# of the picked vertex only if the current
# 			# distance is greater than new distance and
# 			# the vertex in not in the shotest path tree
# 			for v in range(self.V):
# 				if self.graph[u][v] > 0 and \
#                     sptSet[v] == False and \
#                     dist[v] > dist[u] + self.graph[u][v]:
# 					dist[v] = dist[u] + self.graph[u][v]

# 		self.printSolution(dist)


# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
# 		[4, 0, 8, 0, 0, 0, 0, 11, 0],
# 		[0, 8, 0, 7, 0, 4, 0, 0, 2],
# 		[0, 0, 7, 0, 9, 14, 0, 0, 0],
# 		[0, 0, 0, 9, 0, 10, 0, 0, 0],
# 		[0, 0, 4, 14, 10, 0, 2, 0, 0],
# 		[0, 0, 0, 0, 0, 2, 0, 1, 6],
# 		[8, 11, 0, 0, 0, 0, 1, 0, 7],
# 		[0, 0, 2, 0, 0, 0, 6, 7, 0]
# 		]

# g.dijkstra(0)

# # This code is contributed by Divyanshu Mehta
