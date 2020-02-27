from collections import deque
from algos.tree.BST import BST


def level_order_traversal(root):
    if root:
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            print(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


def zig_zag_order_traversal(root):
    left_to_right = True
    if root:
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            print(curr.data)
            if left_to_right:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            left_to_right = not left_to_right


def print_level_averages(root):
    result = []
    if root:
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            sum = 0.0
            for _ in range(size):
                currNode = queue.popleft()
                sum += currNode.data
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            result.append(sum/size)
    return result




def print_left_view(root):
    if root:
        queue = []
        queue.append(root)
        while len(queue):
            size = len(queue)
            for i in range(1,size+1):
                temp = queue[0]
                queue.pop(0)
                if i == size:
                    print(temp.data)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)






tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)
tree.print_bst()
print()