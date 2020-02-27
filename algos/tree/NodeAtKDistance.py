from algos.tree.BST import BST

def node_at_k_distance(root, index=0, arr=[]):
    if root is None:
        return False

    if index == 0:
        arr.append(root.data)
        return True

    node_at_k_distance(root.left, index-1, arr)
    node_at_k_distance(root.right, index-1, arr)

    return False

def find_path_backtrack(root, key, arr):
    if root is None:
        return False

    arr.append(root.data)

    if root.data == key:
        return True

    if find_path_backtrack(root.left, key, arr) or find_path_backtrack(root.right, key, arr):
        arr.append(root.data)
        return True

    # if reached this far nothing to look for then and start popping
    arr.pop(-1)
    return False


counter = 0

def find_kmax_in_bst(root, k):
    global counter
    if root is None:
        return None
    if k == counter:
        return root
    node = find_kmax_in_bst(root.right, k)
    if counter is not k:
        counter += 1
        node = root
    if counter == k:
        return node
    else:
        return find_kmax_in_bst(root.left, k)


def find_duplicates_in_tree(root, str_set=set([])):
    if root is None:
        return ""

    node_str = find_duplicates_in_tree(root.left,str_set)+str(root.data)+find_duplicates_in_tree(root.right, str_set)

    if str_set.__contains__(node_str):
        print('came')
        return ""
    str_set.add(node_str)
    return node_str




tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)
print(find_kmax_in_bst(tree.root, 1).data)
print(find_duplicates_in_tree(tree.root))
