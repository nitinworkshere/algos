from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def level_order_successor(root, key):
    if root:
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    if curr_node.val == key:
                        return curr_node.left.val
                    else:
                        queue.append(curr_node.left)
                if curr_node.right:
                    if curr_node.val == key:
                        return curr_node.right.val
                    else:
                        queue.append(curr_node.right)
        return -1
    else:
        return -1



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(level_order_successor(root, 1))






