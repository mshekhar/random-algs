import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []
        res = []
        if not nums2 or not nums1:
            return res
        for i in xrange(len(nums1)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        i = 0
        while min_heap and i < k:
            val, idx_1, idx_2 = heapq.heappop(min_heap)
            res.append([nums1[idx_1], nums2[idx_2]])
            if idx_2 + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[idx_1] + nums2[idx_2 + 1], idx_1, idx_2 + 1))
            i += 1
        return res


print Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
print Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
print Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3)
print Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 10)
