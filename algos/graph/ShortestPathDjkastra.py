from math import inf

class Graph:

    def __init__(self, V, graph):
        self.V = V
        self.graph = graph

def find_shortest_from_src(graph, src):

    distance = [inf for _ in range(graph.V)]
    visited = [False for _ in range(graph.V)]

    distance[src] = 0

    for start in range(graph.V):
        u = find_min_path_node(graph, distance, visited)
        visited[u] = True

        for v in range(graph.V):
            if graph[u][v] >0 and not visited[v] and distance[v] > distance[u] + graph[u][v]:
                distance[v] = distance[u] + graph[u][v]


def find_min_path_node(graph, dist, visited):
    min_path = inf
    min_node = None
    for node in range(graph.V):
        if dist[node] < min_path and not visited[node]:
            min_path = dist[node]
            min_node = node

    return min_node