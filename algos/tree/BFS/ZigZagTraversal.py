from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def zigzag_traversal(root):
    result = []
    left_to_right = True
    if root:
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level = deque()
            for _ in range(level_size):
                current_node = queue.popleft()
                if left_to_right:
                    level.append(current_node.val)
                else:
                    level.appendleft(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            left_to_right = not left_to_right

            result.append(list(level))
    return result


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.left.left = Node(20)
root.right.left.right = Node(17)
print(zigzag_traversal(root))