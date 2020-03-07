from algos.tree.BST.BST import Node

def unique_bst_2(n):
    if n < 1:
        return []
    return unique_bst_2_rec(1, n)


def unique_bst_2_rec(low, high):
    trees = []
    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high+1):
        ltrees = unique_bst_2_rec(low, i -1)
        rtrees = unique_bst_2_rec(i+1, high)
        print(ltrees)
        print(rtrees)
        for ltree in ltrees:
            for rtree in rtrees:
                root = Node(i)
                root.left = ltree
                root.right = rtree
                trees.append(root)
    return trees


print(unique_bst_2(5))


