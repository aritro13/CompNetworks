import sys 

class Graph(): 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = []

	def graphInput(self):
		for i in range(self.V):
			self.graph.append(list(map(int,input().split())))

	def printSolution(self, dist, path): 
		print ("Vertex \tDistance from Source \tPath")
		for node in range(self.V): 
			print (node, "\t", dist[node],"\t\t\t" ,path[node] )

	def minDistance(self, dist, sptSet): 
		min = sys.maxsize
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 
		return min_index

	def dijkstra(self, src): 
		path = [[]] * self.V
		dist = [sys.maxsize] * self.V 
		print(path)
		dist[src] = 0
		sptSet = [False] * self.V 
		for i in range(self.V): 
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
						# print(v)
						# path[v]= append(u)
						dist[v] = dist[u] + self.graph[u][v] 
		self.printSolution(dist, path) 

n = int(input("Enter No of Vertices: "))
g = Graph(n) 
g.graphInput()
g.dijkstra(0)
