from _collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, x, y):
        self.graph[x].append(y)

    def find_parent(self, parent_arr, x):
        if parent_arr[x] == -1:
            return x
        else:
            return self.find_parent(parent_arr, parent_arr[x])

    def union(self, parent_arr, x, y):
        x_set = self.find_parent(parent_arr, x)
        y_set = self.find_parent(parent_arr, y)

        parent_arr[x_set] = y_set

    def is_cyclic(self):
        parent = [-1 for _ in range(self.V)]

        for v in self.graph:
            for v_adj in self.graph[v]:
                x = self.find_parent(parent, v)
                y = self.find_parent(parent, v_adj)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
print(g.is_cyclic())
