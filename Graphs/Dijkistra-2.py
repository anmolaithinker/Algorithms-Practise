
import heapq
import math

class Graph:

    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(self.v)] for _ in range(self.v)]

    def dijkistra(self,source):

         visited = [False for _ in range(self.v)]
         dist = [math.inf] * self.v
         dist[source] = 0
         l = []
         heapq.heapify(l)
         heapq.heappush(l,0)

         while l!=[]:
             u = heapq.heappop(l)
             print(u)
             visited[u] = True
             for i in range(self.v):
                 if(self.graph[u][i] > 0 and dist[i] > dist[u] + self.graph[u][i] and visited[i] == False):
                     dist[i] = dist[u] + self.graph[u][i]
                     heapq.heappush(l,i)

         for i in range(self.v):
             print("Vertex " + str(i) + " distance : " + str(dist[i]))



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

g.dijkistra(0)