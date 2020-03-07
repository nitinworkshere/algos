from algos.tree.BST.BST import BST

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

counter = 0
def kth_smallest(root, k):
    global counter
    if not root or counter >= k:
        return
    kth_smallest(root.left, k)
    counter += 1
    if k == counter:
        print('Kth minimum is ', root.val)
        return
    kth_smallest(root.right, k)

count = 0
def list_kth_smallest(root, k, arr=[]):
    global count
    if not root or count >= k:
        return
    list_kth_smallest(root.left, k, arr)
    count += 1
    arr.append(root.val)
    if k == count:
        print(arr)
        return
    list_kth_smallest(root.right, k, arr)




bst = BST(10)
bst.insert(bst.root, 20)
bst.insert(bst.root, 2)
bst.insert(bst.root, 4)
bst.insert(bst.root, 80)
bst.insert(bst.root, 40)
kth_smallest(bst.root, 6)
print(list_kth_smallest(bst.root, 6))
