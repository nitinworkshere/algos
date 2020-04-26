from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self, starting_vertex):

        visited = [False for _ in range(len(self.graph))]

        queue = [starting_vertex]

        while queue:
            v = queue.pop(0)
            print(v, " ")
            for curr_vertex in self.graph[v]:
                if not visited[curr_vertex]:
                    queue.append(curr_vertex)
                    visited[curr_vertex] = True

    def dfs(self, starting_vertex):
        visited = [False for _ in range(len(self.graph))]
        self.dfs_helper(starting_vertex, visited)

    def dfs_helper(self, starting_vertex, visited):
        visited[starting_vertex] = True
        print(starting_vertex, "")
        for curr_vertex in self.graph[starting_vertex]:
            if not visited[curr_vertex]:
                self.dfs_helper(curr_vertex, visited)



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.bfs(2)
print()
g.dfs(2)

