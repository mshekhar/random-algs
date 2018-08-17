import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        wages_ratio = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        heap = []
        sum_heap = 0
        res = float('inf')
        for wq, q in wages_ratio:
            heapq.heappush(heap, -q)
            sum_heap += q
            if len(heap) > K:
                sum_heap += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, sum_heap * wq)
        return res


print Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2)
print Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3)
