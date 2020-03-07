from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def min_depth_of_binary_tree(root):
    min_depth = 0
    if root:
        queue = deque()
        queue.append(root)
        while queue:
            min_depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right:
                    return min_depth
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
    return min_depth



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.left.left = Node(20)
root.right.left.right = Node(17)
print(str(min_depth_of_binary_tree(root)))