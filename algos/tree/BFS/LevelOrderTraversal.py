from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def level_order_traversal(root):
    result = []

    if root:
        queue = deque()
        queue.append(root)

        while queue:
            current_level_size = len(queue)
            current_level = []
            for _ in range(current_level_size):
                curr_node = queue.popleft()
                current_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(current_level)
    return result


def reverse_level_order_traversal(root):
    result = deque()

    if root:
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            curr_level = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.appendleft(curr_level)
    return list(result)


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(level_order_traversal(root))
print(reverse_level_order_traversal(root))

