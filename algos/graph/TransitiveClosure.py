#is same as Floyd warshell shortest path b/w nodes with only difference that we dont find min of path but we just check if it exists

from math import inf

class Graph:

    def __init__(self, V, graph):
        self.V = V
        self.graph = graph


def shortest_path_between_vertices(graph):
    dist = [[graph.graph[i][j] for i in range(graph.V)] for j in range(graph.V)]

    for k in range(graph.V):
        for i in range(graph.V):
            for j in range(graph.V):
                dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])

    return dist

g = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]
graph = Graph(4, g)

print(shortest_path_between_vertices(graph))