from algos.graph import Graph

def find_path_using_bfs(graph, source, dest):
    visited = [False for _ in range(graph.V)]
    queue = [source]
    visited[source] = True
    while queue:
        curr_vertex = queue.pop(0)
        if curr_vertex == dest:
            return True
        for i in graph[curr_vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return False





g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)