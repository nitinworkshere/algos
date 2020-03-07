class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

global_sum = 0
def find_max_path_sum(root):
    global global_sum
    if not root:
        return 0

    l = find_max_path_sum(root.left)
    r = find_max_path_sum(root.right)

    max_single = max(max(l, r)+root.val, root.val)
    
    max_top = max(max_single, l+r+root.val)

    global_sum = max(global_sum, max_top)

    return max_single



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
