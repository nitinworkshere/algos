from algos.tree.BST import BST


#go through inorder traversal find first and second misfit node. swap the values
def recover_two_nodes_swapped_tree(root):
    (first, second) = find_nodes_to_be_swapped(root)
    swap(first, second)

def find_nodes_to_be_swapped(root, prev=None, first=None, second=None):
    if root is None:
        return
    find_nodes_to_be_swapped(root.left, prev, first, second)
    if prev.data is not None and prev.data > root.data:
        if first is None:
            first = prev
        second = root
    find_nodes_to_be_swapped(root.right, prev, first, second)
    return first, second

def swap(first, second):
    temp = first
    first = second
    second = temp










tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)