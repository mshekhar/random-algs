import heapq


class HeapObject(object):
    def __init__(self, small_idx, large_idx, small_ele, large_ele):
        self.small_idx = small_idx
        self.large_idx = large_idx
        self.small_ele = small_ele
        self.large_ele = large_ele

    def __cmp__(self, other):
        return cmp(self.small_ele * 1.0 / self.large_ele, other.small_ele * 1.0 / other.large_ele)

    def __str__(self):
        return str(self.small_idx) + "_" + str(self.small_ele) + "_" + str(self.large_idx) + "_" + str(self.large_ele)

    def __repr__(self):
        return str(self.small_idx) + "_" + str(self.small_ele) + "_" + str(self.large_idx) + "_" + str(self.large_ele)


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        min_heap = []
        for c, i in enumerate(A):
            heapq.heappush(min_heap, HeapObject(small_ele=A[0], small_idx=0, large_ele=A[c], large_idx=c))

        k = 1
        # print min_heap
        while k < K:
            ho = heapq.heappop(min_heap)
            k += 1
            # print ho, k
            if ho.small_idx + 1 < len(A) and ho.small_idx + 1 < ho.large_idx:
                ho.small_idx += 1
                ho.small_ele = A[ho.small_idx]
                heapq.heappush(min_heap, ho)

        res = heapq.heappop(min_heap)
        return [res.small_ele, res.large_ele]


print Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3)
print Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 5)
print Solution().kthSmallestPrimeFraction([1, 7], 1)
