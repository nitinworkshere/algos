#1 way is to maintain total count and do insertion sort
# we need to keep first half in max heap and second half in min heap and just do average of the top of both

class RunningMedian:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    if not self.maxHeap or -self.maxHeap[0] >= num:
        heappush(self.maxHeap, -num)
    else:
        heappush(self.minHeap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
        heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
        heappush(self.maxHeap, -heappop(self.minHeap))