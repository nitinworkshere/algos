class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

diameter = 0
def tree_diameter(root):
    global diameter
    if not root:
        return 0
    local_diameter = 1 + (tree_diameter(root.left) + tree_diameter(root.right))

    return max(local_diameter, diameter)



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(tree_diameter(root))