'''
Runtime: 640 ms, faster than 71.40% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 36.1 MB, less than 48.16% of Python3 online submissions for Find Median from Data Stream.
'''
import heapq
# min-Max Heap Template
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            # Always insert into minHeap first, but notice that the item must be the minimum of the maxHeap
            # so, we'll have either equal size of both heaps or minHeap always have the middle item
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
for i in range(10):
    obj.addNum(i + 1)
    print(obj.findMedian())