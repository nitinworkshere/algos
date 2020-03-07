from algos.tree.BST.BST import BST

def least_common_ancestor(root, k1, k2):
    if not root:
        return None

    if root.val == k1 or root.val == k2:
        return root

    key1 = least_common_ancestor(root.left, k1, k2)
    key2 = least_common_ancestor(root.right, k1, k2)

    if key1 and key2:
        return root
    return key1 if key1 else key2



bst = BST(10)
bst.insert(bst.root, 20)
bst.insert(bst.root, 2)
bst.insert(bst.root, 4)
bst.insert(bst.root, 80)
bst.insert(bst.root, 40)
print(least_common_ancestor(bst.root, 4, 40).val)