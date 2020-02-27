from algos.tree.BST import BST

def least_common_ancestor_basic(root, key1, key2):
    path1 = []
    path2 = []
    if not find_path_to_key(root, key1, path1) or not find_path_to_key(root, key2, path2):
        return -1
    lca = 0
    while path1 and path2:
        item1 = path1.pop()
        item2 = path2.pop()
        if item1 == item2:
            lca = item1
        else:
            break
    return lca

def find_path_to_key(root, key, arr):
    if root is None:
        return False

    if root.data == key:
        arr.append(root.data)
        return True
    lfind = find_path_to_key(root.left, key, arr)
    rfind = find_path_to_key(root.right, key, arr)

    if lfind or rfind:
        arr.append(root.data)
        return True

    return False

#look key1 in left subtree and key2 in right subtree where both node returns true to uproot is the lca
def lca_recursive(root, key1, key2):
    if root is None:
        return None
    if root.data == key1 or root.data == key2:
        return root
    left = lca_recursive(root.left, key1, key2)
    right = lca_recursive(root.right, key1, key2)
    if left and right:
        return root
    if not left and not right:
        return None
    return left if left else right



tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)
print(least_common_ancestor_basic(tree.root, 5, 40))

print(lca_recursive(tree.root, 5, 40).data)
