from algos.tree.Node import Node


class BST:

    def __init__(self, data):
        self.root = Node(data)

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def search(self, data):
        if self.root:
            self.root.search(data)
        else:
            return False

    def print_bst(self):
        if self.root is None:
            print('Nothing')
        else:
            self.root.print_node()

    def delete(self, data):
        if self.root is None:
            return None
        else:
            self.root.delete_node(data)

