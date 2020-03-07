class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def check_balanced_tree(root):
    if not root:
        return True
    return abs(height(root.left) - height(root.right)) <= 1 and check_balanced_tree(root.left) and check_balanced_tree(root.right)


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

print(check_balanced_tree(root))
