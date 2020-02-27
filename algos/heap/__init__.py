from algos.heap.MaxHeap import MaxHeap

maxheap = MaxHeap()
maxheap.insert(5)
maxheap.insert(10)
maxheap.insert(2)
maxheap.insert(11)
maxheap.insert(1)
print(maxheap.get_max())
maxheap.remove_max()
maxheap.get_max()
maxheap.insert(30)
print(maxheap.get_max())