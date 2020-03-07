#    1
#   / \
#  2   5
# / \   \
#3   4   6


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def flat_bt_to_ll(root):
    curr = root
    right_stack = []
    while curr or len(right_stack) >= 1:
        if curr.right:
            right_stack.append(curr.right)
        if curr.left:
            curr.right = curr.left
            curr.left = None
        elif len(right_stack) >= 1:
            curr.right = right_stack.pop()
        curr = curr.right


def print_flat_ll(root):
    if root:
        print(root.val)
        print_flat_ll(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
flat_bt_to_ll(root)
print_flat_ll(root)


