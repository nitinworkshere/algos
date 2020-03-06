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
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    return dist


g = [[0,5,inf,10],
             [inf, 0, 3,inf],
             [inf, inf, 0, 1],
             [inf, inf, inf, 0]
        ]
graph = Graph(4, g)
print(shortest_path_between_vertices(graph))