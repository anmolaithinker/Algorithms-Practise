
import math

class Graph:

    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def minDistance(self , dist , visited):
        min = math.inf
        for i in range(self.v):
            if(not visited[i]):
                if(dist[i]<min):
                    min = i
        return min


    def printSol(self,dist):
        for i in range(self.v):
            print(str(i) + " :::::---> " + str(dist[i]))

    def Dijkistra(self,source):

        dist = [math.inf] * self.v
        visited = [False for _ in range(self.v)]

        dist[source] = 0

        for i in range(self.v):
            u = self.minDistance(dist,visited)
            print("Min : " + str(u))
            visited[u] = True
            for j in range(self.v):
                if(self.graph[u][j]>0 and dist[j] >= dist[u] + self.graph[u][j] and visited[j] == False):
                    print ("True For j : " + str(j))
                    dist[j] = dist[u] + self.graph[u][j]

        self.printSol(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.Dijkistra(0)