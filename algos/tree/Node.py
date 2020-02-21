class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data < data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data)
        if self.data > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        return

    def search(self, data):
        if self.data < data:
            if self.right is not None:
                self.right.search(data)
            else:
                return False
        if self.data > data:
            if self.left is not None:
                self.left.search(data)
            else:
                return False
        return True

    def print_node(self):
        if self.left:
            self.left.print_node()
        print(self.data)
        if self.right:
            self.right.print_node()

    def delete_node(self, data):
        if self.data < data:
            if self.right is not None:
                self.right = self.right.delete_node(data)
            else:
                return self
        if self.data > data:
            if self.left is not None:
                self.left = self.left.delete_node(data)
            else:
                return self
        else:
            if self.right is None and self.left is None:
                self = None
            elif self.right is None:
                tmp = self.left
                self.left = None
                return tmp
            elif self.left is None:
                tmp = self.right
                self.right = None
                return tmp
            else: #where both are not none
                curr = self.right
                while curr is not None:
                    curr = curr.left
                self.data = curr.data
                self.right = self.right.delete_node(curr.data) #trick where we have curr data copied to node to be deleted and all we need to get rid of is duplicate node




