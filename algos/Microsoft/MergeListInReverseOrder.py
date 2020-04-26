# Given two sorted non-empty linked lists. Merge them in
# such a way that the result list will be in reverse
# order. Reversing of linked list is not allowed. Also,
# extra space should be O(1)

# Node of a linked list
class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    # Given two non-empty linked lists 'a' and 'b'


def SortedMerge(a, b):
    # If both lists are empty
    if (a == None and b == None):
        return None

    # Initialize head of resultant list
    res = None

    # Traverse both lists while both of then
    # have nodes.
    while (a != None and b != None):

        # If a's current value is smaller or equal to
        # b's current value.
        if (a.key <= b.key):

            # Store next of current Node in first list
            temp = a.next

            # Add 'a' at the front of resultant list
            a.next = res
            res = a

            # Move ahead in first list
            a = temp

        # If a's value is greater. Below steps are similar
        # to above (Only 'a' is replaced with 'b')
        else:

            temp = b.next
            b.next = res
            res = b
            b = temp

        # If second list reached end, but first list has
    # nodes. Add remaining nodes of first list at the
    # front of result list
    while (a != None):
        temp = a.next
        a.next = res
        res = a
        a = temp

    # If first list reached end, but second list has
    # node. Add remaining nodes of first list at the
    # front of result list
    while (b != None):
        temp = b.next
        b.next = res
        res = b
        b = temp

    return res


# Function to print Nodes in a given linked list
def printList(Node):
    while (Node != None):
        print(Node.key, end=" ")
        Node = Node.next


# Utility function to create a new node with
# given key
def newNode(key):
    temp = Node()
    temp.key = key
    temp.next = None
    return temp


# Driver program to test above functions

# Start with the empty list
res = None

# Let us create two sorted linked lists to test
# the above functions. Created lists shall be
#	 a: 5.10.15
#	 b: 2.3.20
a = newNode(5)
a.next = newNode(10)
a.next.next = newNode(15)

b = newNode(2)
b.next = newNode(3)
b.next.next = newNode(20)

print("List A before merge: ")
printList(a)

print("\nList B before merge: ")
printList(b)

# merge 2 increasing order LLs in descresing order
res = SortedMerge(a, b)

print("\nMerged Linked List is: ")
printList(res)

# This code is contributed by Arnab Kundu
