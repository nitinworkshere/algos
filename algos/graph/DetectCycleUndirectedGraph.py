from algos.graph.Graph import Graph

def find_cycle_util(graph, vertex, visited = {}, parent=None):
    visited[vertex] = True

    for i in graph[vertex]:
        if not visited[i]:
            if find_cycle_util(graph, i, visited, vertex):
                return True
        elif parent != i:
            return True
    return False
