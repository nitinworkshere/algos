from algos.List.Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.get_head() is None

    def insert_node(self, data):
        if self.is_empty():
            self.head = Node(data)
            return self.head
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
            return temp

    def print_list(self):
        temp = self.get_head()
        while temp is not None:
            print(temp.data, '->')
            temp = temp.next

