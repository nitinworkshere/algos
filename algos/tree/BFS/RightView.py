from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def print_right_view(root):
    result = []
    if root:
        queue = deque()
        queue.append(root)
        curr_node = None
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(curr_node.val)
    return result

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.left.left.left = Node(3)
print(print_right_view(root))