from algos.graph.Graph import Graph

def detect_cycle(graph, start_vertex):
    visited = []
    recursion_stack = []
    detect_cycle_helper(graph, start_vertex, visited, recursion_stack)


def detect_cycle_helper(graph, start_vertex, visited, recursion_stack):
    visited[start_vertex] = True
    recursion_stack[start_vertex] = True

    for curr_vertex in graph[start_vertex]:
        if not visited[curr_vertex]:
            detect_cycle_helper(graph, curr_vertex, visited, recursion_stack)
        elif recursion_stack[curr_vertex]:
            return True

        recursion_stack[start_vertex] = False
        return False


