class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def recover_bst_with_swapped_node(root):
    find_nodes_to_be_swapped(root)
    print(first.val, second.val)


prev, first, second = None, None, None


def find_nodes_to_be_swapped(root):
    global prev, first, second
    if not root:
        return
    find_nodes_to_be_swapped(root.left)
    if prev:
        if prev.val > root.val:
            if not first:
                first = prev
            second = root
    prev = root
    find_nodes_to_be_swapped(root.right)


root = Node(1)
root.left = Node(3)
root.left.right = Node(2)
recover_bst_with_swapped_node(root)
