class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def sum_path_numbers(root, pathsum = 0):
    if not root:
        return 0
    pathsum = pathsum*10 + root.val

    if not root.left and not root.right:
        return pathsum

    return sum_path_numbers(root.left, pathsum) + sum_path_numbers(root.right, pathsum)



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(sum_path_numbers(root))