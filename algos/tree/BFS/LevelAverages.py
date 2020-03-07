from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def level_averages(root):
    result = []
    if root:
        queue = deque()
        queue.append(root)

        while queue:
            current_level_size = len(queue)
            current_level_sum = 0.0
            for _ in range(current_level_size):
                curr_node = queue.popleft()
                current_level_sum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(current_level_sum/current_level_size)

    return result




root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(level_averages(root))