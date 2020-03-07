class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def invert_tree(root):
    if root:
        root.left = invert_tree(root.right)
        root.right = invert_tree(root.left)
    return root

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print_tree(root)
invert_tree(root)
print()
print_tree(root)
