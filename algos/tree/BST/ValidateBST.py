from algos.tree.BST.BST import BST
from math import inf

def validate_bst(root):
    return validate_bst_recursion(root)

def validate_bst_recursion(root, leftbound = -inf, rightbound = inf):
    if root:
        if (leftbound and leftbound >= root.val) or (rightbound and rightbound <= root.val):
            return False
        return validate_bst_recursion(root.right, root.val, rightbound) and (validate_bst_recursion(root.left, leftbound, root.val))
    else:
        return True



bst = BST(10)
bst.insert(bst.root, 20)
bst.insert(bst.root, 2)
bst.insert(bst.root, 4)
bst.insert(bst.root, 80)
bst.insert(bst.root, 40)
print(validate_bst(bst.root))

