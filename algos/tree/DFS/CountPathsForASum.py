class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def count_paths_recursive(currentNode, S, currentPath=[]):
    if currentNode is None:
        return 0

    # add the current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count.
        if pathSum == S:
            pathCount += 1

    # traverse the left sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    # traverse the right sub-tree
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(count_paths_recursive(root, 28))
