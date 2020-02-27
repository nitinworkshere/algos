
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.swim_up(len(self.heap)-1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def remove_max(self):
        if self.heap:
            if len(self.heap) > 1:
                self.heap[0] = self.heap[-1]
                del self.heap[-1]
                self.sink_down(0)
            else:
                del self.heap[0]
        else:
            return None

    def swim_up(self, index):
        if index <= 0:
            return
        parent = (index-1)//2
        if self.heap[parent] < self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.swim_up(parent)

    def sink_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            self.sink_down(largest)

