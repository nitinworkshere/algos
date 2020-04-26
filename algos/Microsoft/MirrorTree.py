# Python3 program to convert a binary
# tree to its mirror

# Utility function to create a new
# tree node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



def mirror_rec(node):
    if not node:
        return
    else:

        temp = node

        """ do the subtrees """
        mirror_rec(node.left)
        mirror_rec(node.right)

        """ swap the pointers in this node """
        temp = node.left
        node.left = node.right
        node.right = temp





def mirror_iterative(root):
    if (root == None):
        return

    q = [root]

    # Do BFS. While doing BFS, keep swapping
    # left and right children
    while q:

        # pop top node from queue
        curr = q.pop(0)

        # swap left child with right child
        curr.left, curr.right = curr.right, curr.left

        # append left and right children
        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)


""" Helper function to print Inorder traversal."""
def inOrder( node):
    if (node == None):
        return
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)


# Driver code
if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)

    """ Print inorder traversal of 
        the input tree """
    print("Inorder traversal of the",
          "constructed tree is")
    inOrder(root)

    """ Convert tree to its mirror """
    mirror(root)

    """ Print inorder traversal of 
        the mirror tree """
    print("\nInorder traversal of",
          "the mirror treeis ")
    inOrder(root)

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
