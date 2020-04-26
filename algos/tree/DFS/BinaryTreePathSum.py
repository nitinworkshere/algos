#complexity O(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def check_if_path_sum(root, sum):
    if sum == 0:
        return True
    if not root:
        return False
    return check_if_path_sum(root.left, sum - root.val) or check_if_path_sum(root.right, sum - root.val)

#This is a backtrack problem as we dont want to exit simply after finding one solution, we want to try other options too

def print_all_path_sum(root, sum):
    paths = []
    print_all_path_sum_rec(root, sum, [], paths)
    return paths


def print_all_path_sum_rec(root, sum, current_path, paths):

    if not root:
        return

    current_path.append(root.val)

    if root.val == sum and root.left is None and root.right is None: #This condition checks for root to leaf if removed it will be subpath
        paths.append(list(current_path))
    else:
        print_all_path_sum_rec(root.left, sum - root.val, current_path, paths)
        print_all_path_sum_rec(root.right, sum - root.val, current_path, paths)

    del current_path[-1] #coming to this line means this node was not contributing to path sum other wise call have returned above only



root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(check_if_path_sum(root, 12))
print(print_all_path_sum(root, 23))