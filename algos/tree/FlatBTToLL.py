
#one way can be bfs way
def flat_bt_to_ll(root):
    if root:
        lnode = flat_bt_to_ll(root.left)
        rnode = flat_bt_to_ll(root.right)

        #do the swap and set left to null
        root.right = root.left
        lnode.right = rnode
        root.left = None
