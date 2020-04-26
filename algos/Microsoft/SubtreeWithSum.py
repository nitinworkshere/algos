# Python3 implementation to count subtress
# that Sum up to a given value x

# class to get a new node
class getNode:
    def __init__(self, data):
        # put in the data
        self.data = data
        self.left = self.right = None


# function to count subtress that
# Sum up to a given value x
def countSubtreesWithSumX(root, count, x):
    # if tree is empty
    if (not root):
        return 0

    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)

    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)

    # Sum of nodes in the subtree
    # rooted with 'root.data'
    Sum = ls + rs + root.data

    # if true
    if (Sum == x):
        count[0] += 1

    # return subtree's nodes Sum
    return Sum


# utility function to count subtress
# that Sum up to a given value x
def countSubtreesWithSumXUtil(root, x):
    # if tree is empty
    if (not root):
        return 0

    count = [0]

    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)

    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)

    # if tree's nodes Sum == x
    if ((ls + rs + root.data) == x):
        count[0] += 1

    # required count of subtrees
    return count[0]


# Driver Code
if __name__ == '__main__':
    # binary tree creation
    #		 5
    #		 / \
    #	 -10	 3
    #	 / \ / \
    #	 9 8 -4 7
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)

    x = 7

    print("Count =",
          countSubtreesWithSumXUtil(root, x))

# This code is contributed by PranchalK
