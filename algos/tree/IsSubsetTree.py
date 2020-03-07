class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def is_subset(root1, root2):
    if not root1:
        return False
    if not root2:
        return True
    if are_identical(root1, root2):
        return True
    return is_subset(root1.left, root2) or is_subset(root1.right, root2)

def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

root2 = Node(7)
root2.left = Node(9)

print(is_subset(root,root2))
