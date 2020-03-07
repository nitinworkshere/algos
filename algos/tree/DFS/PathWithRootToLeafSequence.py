class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def path_with_sequence(root, sequence, index = 0):
    if not root:
        return False
    if index >= len(sequence) or sequence[index] != root.val:
        return False
    if not root.left and not root.right and index == len(sequence)-1:
        return True
    return path_with_sequence(root.left, sequence, index+1) or path_with_sequence(root.right, sequence, index+1)



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

print(path_with_sequence(root, [12,7,9]))