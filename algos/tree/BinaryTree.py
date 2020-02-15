class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def search(self, data):
        if self.data > data:
            if self.left is None:
                return print('Not found')
            else:
                return self.left.search(data)
        if self.data < data:
            if self.right is None:
                return print('Not found')
            else:
                return self.right.search(data)
        else:
            print('found')




    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

