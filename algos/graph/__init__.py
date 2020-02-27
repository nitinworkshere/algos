from algos.graph.Graph import Graph
from algos.graph.GraphAlgorithms import GraphAlgorithms

graph = Graph(5)
graph.add_edge(4,1)
graph.add_edge(4,2)
graph.add_edge(0,1)
graph.add_edge(0,4)
graph.add_edge(1,2)
graph.add_edge(3,0)

# graph.print()
# print()
# print()
#
# GraphAlgorithms.bfs(graph, 0)
#
# print()
# print()
#
# GraphAlgorithms.dfs(graph, 0)
#
# print()
# print()

GraphAlgorithms.detect_cycle(graph)

