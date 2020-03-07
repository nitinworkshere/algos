class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, root, val):
        if root:
            if root.val > val:
                if root.left:
                    self.insert(root.left, val)
                else:
                    root.left = Node(val)
            else:
                if root.right:
                    self.insert(root.right, val)
                else:
                    root.right = Node(val)
        else:
            self.root = Node(val)

    def print_bst(self, root):
        if root:
            self.print_bst(root.left)
            print(root.val)
            self.print_bst(root.right)

