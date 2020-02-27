from algos.graph.Graph import Graph
from algos.graph.Queue import Queue


class GraphAlgorithms:

#in case of recursive bfs we will make queue part of function

    @staticmethod
    def bfs(graph, vertex):
        queue = Queue()
        queue.queue(vertex)

        while not queue.is_empty():
            current_vertex = queue.dequeue()
            print(current_vertex)
            if graph:
                destlist = graph.arr[current_vertex]
                current_dest = destlist.get_head()

                while current_dest is not None:
                    queue.queue(current_dest.val)
                    current_dest = current_dest.next

        return


#either stack or use recursive call to print
    @staticmethod
    def dfs(graph, vertex):
        print(vertex)

        curr_dest_head = graph.arr[vertex].get_head()
        while curr_dest_head is not None:
            GraphAlgorithms.dfs(graph, curr_dest_head.val)
            curr_dest_head = curr_dest_head.next

        return

    @staticmethod
    def detect_cycle(graph, current_vertex=0, visited=[None]*5):
        if visited[current_vertex] is not None:
            print('a dag')
            return True
        else:
            visited[current_vertex] = True
            current_dest_head = graph.arr[current_vertex].get_head()
            while current_dest_head is not None:
                if GraphAlgorithms.detect_cycle(graph, current_dest_head.val, visited):
                    return True
                current_dest_head = current_dest_head.next

        return False





