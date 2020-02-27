from algos.tree.BST import BST


def check_if_path_sum(root, sum):
    if root is None:
        return False
    if root.data == sum:
        return True
    if root:
        return check_if_path_sum(root.left, sum - root.data) or check_if_path_sum(root.right, sum - root.data)

def print_all_paths_with_sum(root, sum, currentpath=[], allpaths=[]):
    if root is None:
        return

    currentpath.append(root.data)

    if root.data == sum:
        allpaths.append(list(currentpath)) # make array of lists
    else:
        print_all_paths_with_sum(root.left, sum - root.data, currentpath, allpaths)
        print_all_paths_with_sum(root.right, sum - root.data, currentpath, allpaths)
    del currentpath[-1] # with each flow returning back after non matching we will need to keep on removing last element in list





tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)
print(check_if_path_sum(tree.root, 60))