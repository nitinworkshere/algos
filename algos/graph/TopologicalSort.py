#Time and space complexity O(V+E)


def topological_sort(vertices, edges):
    sortedOrder = []
    graph = {i:[] for i in range(vertices)}
    indegree = {i:0 for i in range(vertices)}

    for edge in edges:
        (parent, child) = edge[0], edge[1]
        graph[parent].append(child)
        indegree[child] += 1

    sources = []
    for key in indegree:
        if indegree[key] is 0:
            sources.append(key)

    while sources:
        source = sources.pop(0)
        sortedOrder.append(source)
        for adj_node in graph[source]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                sources.append(adj_node)

    return sortedOrder


print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))

