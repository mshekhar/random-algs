from heapq import heappush, heappop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        if not self.max_heap:
            heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                heappush(self.max_heap, -num)
                if len(self.max_heap) > len(self.min_heap) + 1:
                    heappush(self.min_heap, -heappop(self.max_heap))
            else:
                heappush(self.min_heap, num)
                if len(self.min_heap) > len(self.max_heap):
                    heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """

        return (-self.max_heap[0] + self.min_heap[0]) / 2.0 \
            if len(self.min_heap) == len(self.max_heap) \
            else -self.max_heap[0]


# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print obj.findMedian()
# obj.addNum(3)
# print obj.max_heap, obj.min_heap
# print obj.findMedian()
