from algos.tree.BST import BST
from algos.tree.Node import Node

def mirror_image(root):
    if root:
        mirror_image(root.left)
        mirror_image(root.right)
        temp = root.right
        root.right = root.left
        root.left = temp


def sorted_list_to_bst(lst):
    if lst:
        half = len(lst)//2
        root = Node(lst[half])
        root.left = sorted_list_to_bst(lst[:half])
        root.right = sorted_list_to_bst(lst[half+1:])
        return root

    return None


def convert_bst_from_post_pre(root, pre, post):
    if pre and post:
        root = Node(pre[0])
        if len(pre) == 1:
            return root

        #find index of next of pre in post to divide into two chunks
        l = post.index[pre[1]]
        root.left = convert_bst_from_post_pre(pre[1:l+1], post[:l])
        root.right = convert_bst_from_post_pre(pre[l+1:], post[l:-1])
        return root







tree = BST(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(2)
tree.print_bst()
print(mirror_image(tree.root))
tree.print_bst()

lst = [10,20,30,40,50,100,300]
converted_tree = BST(sorted_list_to_bst(lst))
