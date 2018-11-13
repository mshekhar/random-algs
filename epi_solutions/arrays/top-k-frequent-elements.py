import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k < 1:
            return []
        nums_counter = collections.Counter(nums)
        min_heap = []
        for num, count in nums_counter.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res[::-1]


print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print Solution().topKFrequent([1], 1)
