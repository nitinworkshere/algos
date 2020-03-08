import collections
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None



def print_vertical_tree(root, root_distances={}, distances={}):
    if not root:
        return

    queue = []
    queue.append(root)
    root_distances[root] = 0
    distances[0] = [root.val]

    while len(queue)>0:
        current = queue.pop(0)

        if current.left:
            queue.append(current.left)

            root_distances[current.left] = root_distances[current] - 1
            distance = root_distances[current.left]

            if not distances.get(distance):
                distances[distance] = []
            distances[distance].append(current.left.val)

        if current.right:
            queue.append(current.right)

            root_distances[current.right] = root_distances[current] + 1
            distance = root_distances[current.right]

            if not distances.get(distance):
                distances[distance] = []
            distances[distance].append(current.right.val)

        sorted_distances = collections.OrderedDict(sorted(distances.items()))

        for i in sorted_distances.values():
            for j in i:
                print(j)
            print()





root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
print_vertical_tree(root)