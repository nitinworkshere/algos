
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def convert_to_bst(arr):
    if len(arr) < 1:
        return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = convert_to_bst(arr[:mid])
    root.right = convert_to_bst(arr[mid+1:])
    return root

def print_bst(root):
    if root:
        print_bst(root.left)
        print(root.val)
        print_bst(root.right)

print_bst(convert_to_bst([-10,-3,0,5,9]))


