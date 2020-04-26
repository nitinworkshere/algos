#! /usr/bin/env python3

# connect nodes at same level using level order traversal
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

    def __str__(self):
        return '{}'.format(self.data)


def printLevelByLevel(root):
    # print level by level
    if root:
        node = root
        while node:
            print('{}'.format(node.data), end=' ')
            node = node.nextRight
        print()
        if root.left:
            printLevelByLevel(root.left)
        else:
            printLevelByLevel(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def connect(root):
    # set nextRight of all nodes of a tree
    queue = []
    queue.append(root)
    # null marker to represent end of current level
    queue.append(None)
    # do level order of tree using None markers
    while queue:
        p = queue.pop(0)
        if p:
            # next element in queue represents
            # next node at current level
            p.nextRight = queue[0]
            # pus left and right children of current node
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        elif queue:
            queue.append(None)


def main():
    """Driver program to test above functions.
        Constructed binary tree is
                10
            / \
            8	 2
            /	 \
        3		 90
    """

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(90)

    # Populates nextRight pointer in all nodes
    connect(root)

    # Let us check the values of nextRight pointers
    print("Following are populated nextRight pointers in \n"
          "the tree (-1 is printed if there is no nextRight) \n")
    if (root.nextRight != None):
        print("nextRight of %d is %d \n" % (root.data, root.nextRight.data))
    else:
        print("nextRight of %d is %d \n" % (root.data, -1))
    if (root.left.nextRight != None):
        print("nextRight of %d is %d \n" % (root.left.data, root.left.nextRight.data))
    else:
        print("nextRight of %d is %d \n" % (root.left.data, -1))
    if (root.right.nextRight != None):
        print("nextRight of %d is %d \n" % (root.right.data, root.right.nextRight.data))
    else:
        print("nextRight of %d is %d \n" % (root.right.data, -1))
    if (root.left.left.nextRight != None):
        print("nextRight of %d is %d \n" % (root.left.left.data, root.left.left.nextRight.data))
    else:
        print("nextRight of %d is %d \n" % (root.left.left.data, -1))
    if (root.right.right.nextRight != None):
        print("nextRight of %d is %d \n" % (root.right.right.data, root.right.right.nextRight.data))
    else:
        print("nextRight of %d is %d \n" % (root.right.right.data, -1))

    print()


if __name__ == "__main__":
    main()

# This code is contributed by Ram Basnet
