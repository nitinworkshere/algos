

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.get_head() is None

    def insert_node(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)

#This has cycle never tells you about start of cycle as in ring these pointers can catch up any time
#For cycle length K to find start we will need to move fast pointer by k
    def has_cycle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def print_list(self):
        temp = self.get_head()
        while temp is not None:
            print(temp.data, '->', temp.next.data if temp.next is not None else None)
            temp = temp.next
