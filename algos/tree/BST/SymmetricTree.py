class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def symetric_tree(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return root1.val == root2.val and symetric_tree(root1.left, root2.right) and symetric_tree(root1.right, root2.left)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(4)
root.left.left = Node(3)
root.right.right = Node(3)
root.right.left = Node(4)

print(symetric_tree(root.left, root.right))