
import math

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def BellmanFord(self,source):

        dist = [math.inf for _ in range(self.v)]
        dist[source] = 0

        for _ in range(self.v-1):
            for u,v,w in self.graph:
                if(dist[u]!=math.inf and dist[v] > dist[u] + w):
                    dist[v] = dist[u] + w

        print("Checking if graph contains -ve weight cycle ::::::::::: ")
        print ('-' * 100)

        for u,v,w in self.graph:
            if(dist[v] > dist[u] + w):
                print("Negative weight is present in the graph")
                break


        print('-' * 100)

        print("---------------------RESULT------------------")
        print ('-' * 100)
        for i in range(self.v):
            print( " Vertex : " + str(i) + " -> " + str(dist[i]))


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.BellmanFord(0)








