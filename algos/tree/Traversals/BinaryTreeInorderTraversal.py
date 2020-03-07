class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def binary_tree_inorder_traversal(root, lst=[]):
    if root:
        binary_tree_inorder_traversal(root.left)
        lst.append(root.val)
        binary_tree_inorder_traversal(root.right)
    return lst



root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(binary_tree_inorder_traversal(root))