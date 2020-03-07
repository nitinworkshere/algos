class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def identical_tree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and identical_tree(root1.left, root2.left) and identical_tree(root1.right, root2.right)


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)


root1 = Node(12)
root1.left = Node(7)
root1.right = Node(1)
root1.left.left = Node(9)
root1.right.left = Node(10)
root1.right.right = Node(5)

print(identical_tree(root, root1))
