# Class to create a new Tree Node
class newNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def inorder(root: newNode):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def merge(root1: newNode, root2: newNode):
    # s1 is stack to hold nodes of first BST
    s1 = []

    # Current node of first BST
    current1 = root1

    # s2 is stack to hold nodes of first BST
    s2 = []

    # Current node of second BST
    current2 = root2

    # If first BST is empty then the output is the
    # inorder traversal of the second BST
    if not root1:
        return inorder(root2)

    # If the second BST is empty then the output is the
    # inorder traversal of the first BST
    if not root2:
        return inorder(root1)

    # Run the loop while there are nodes not yet printed.
    # The nodes may be in stack(explored, but not printed)
    # or may be not yet explored
    while current1 or s1 or current2 or s2:

        # Following steps follow iterative Inorder Traversal
        if current1 or current2:

            # Reach the leftmost node of both BSTs and push ancestors of
            # leftmost nodes to stack s1 and s2 respectively
            if current1:
                s1.append(current1)
                current1 = current1.left

            if current2:
                s2.append(current2)
                current2 = current2.left

        else:

            # If we reach a NULL node and either of the stacks is empty,
            # then one tree is exhausted, ptint the other tree

            if not s1:
                while s2:
                    current2 = s2.pop()
                    current2.left = None
                    inorder(current2)
                    return
            if not s2:
                while s1:
                    current1 = s1.pop()
                    current1.left = None
                    inorder(current1)
                    return

            # Pop an element from both stacks and compare the
            # popped elements
            current1 = s1.pop()
            current2 = s2.pop()

            # If element of first tree is smaller, then print it
            # and push the right subtree. If the element is larger,
            # then we push it back to the corresponding stack.
            if current1.data < current2.data:
                print(current1.data, end=" ")
                current1 = current1.right
                s2.append(current2)
                current2 = None

            else:
                print(current2.data, end=" ")
                current2 = current2.right
                s1.append(current1)
                current1 = None


# Driver code

def main():
    # Let us create the following tree as first tree
    #	 3
    #	 / \
    # 1 5

    root1 = newNode(3)
    root1.left = newNode(1)
    root1.right = newNode(5)

    # Let us create the following tree as second tree
    #	 4
    #	 / \
    # 2 6
    #

    root2 = newNode(4)
    root2.left = newNode(2)
    root2.right = newNode(6)

    merge(root1, root2)


if __name__ == "__main__":
    main()

# This code is contributed by Koushik Reddy Bukkasamudram
