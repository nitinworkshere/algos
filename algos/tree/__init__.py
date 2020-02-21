from algos.tree.BST import BST
from algos.tree.BSTAlgorithms import BSTAlgorithms

#root = Node(10)
#root.insert(20)
#root.insert(5)
#root.insert(7)
#root.printtree()
#print(root.min_value())


root = BST(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(5)
root.insert(7)
root.insert(1)
root.insert(2)
#root.print_bst()
print(flush=True)
#root.print_bst()
print(flush=True)
#print(BSTAlgorithms.findheight(root.root))
arr = []
#BSTAlgorithms.findancestor(root.root, 40, arr)
BSTAlgorithms.recfindacestor(root.root, 40, arr)
print(str(arr))
level = []
BSTAlgorithms.recnodeatkdistance(root.root, 4, 1, level)
print(str(level))








