from algos.graph.Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_at_tail(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        return

    def insert_at_head(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return self.head

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self.head

    def delete(self, key):
        if self.head is None:
            print('List is empty')
            return False
        temp = self.head
        while temp.next is not None:
            if temp.val == key:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del temp
                return True

    def search(self, key):

        if self.head is None:
            print('list is empty')
            return None

        temp = self.head
        while temp.next is not None:
            if temp.val == key:
                return temp
            temp = temp.next
        print(key, " not is list")
        return None

    def print(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                print(temp.val)
                temp = temp.next
            print(temp.val)
            return True
        else:
            print('List is empty')
            return False


