from algos.graph.LinkedList import LinkedList


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.arr = []

        for i in range(vertices):
            temp = LinkedList()
            self.arr.append(temp)

    def add_edge(self, source, dest):
        self.arr[source].insert_at_head(dest) #will keep on appending new edge dest on head of linked list

    def print(self):
        for vertex in range(self.vertices):
            print("|", vertex, end=" | => ")
            dest = self.arr[vertex].get_head()
            while dest is not None:
                print("[" , dest.val, end = " ] -> ")
                dest = dest.next
            print("None")