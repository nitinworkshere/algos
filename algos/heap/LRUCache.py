from algos.heap.Node import Node

class LRUCache:

    def __init__(self, capacity=0, keys={}): #map contains <data, Node>
        self.capacity = capacity
        self.keys = keys
        self.head = None
        self.tail = None


    def get(self, key):
        if self.keys[key] is None:
            return -1
        node_to_put = self.keys[key]
        self.remove_node(node_to_put)
        self.insert_node(node_to_put)

        return node_to_put.value


    def put(self, key, value):
        if self.keys[key] is not None:
            node_to_put = self.keys[key]
            node_to_put.value = value

            self.remove_node(node_to_put)
            self.put(node_to_put)
        else:
            if len(self.keys) >= self.capacity:
                del self.keys[key]
                self.remove_node(self.head)
            node_to_put = Node(key, value)
            self.insert_node(node_to_put)
            self.keys[key] = node_to_put

    def remove_node(self, node):
        if node.prev is None: #head node case
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None: #tail node case
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def insert_node(self, node):
        #insert into tail and if head none then tail was also none
        if self.tail:
            self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        if self.head is None:
            self.head = self.tail
