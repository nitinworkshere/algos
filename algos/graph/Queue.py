class Queue:

    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def queue(self, val):
        self.queue_list.append(val)

    def front(self):
        if not self.is_empty():
            return self.queue_list[0]
        else:
            return None

    def back(self):
        if not self.is_empty():
            return self.queue_list[-1]
        else:
            return None

    def dequeue(self):
        if not self.is_empty():
            front = self.front()
            self.queue_list.remove(self.front())
            return front
        else:
            return None

