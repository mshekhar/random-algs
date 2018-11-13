import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        min_heap = []
        ugly_nums = [1] * n
        for c, prime in enumerate(primes):
            heapq.heappush(min_heap, (prime, prime, 0))
        i = 1
        while i < n:
            ugly_nums[i] = min_heap[0][0]
            while min_heap and min_heap[0][0] == ugly_nums[i]:
                val, prime, idx = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (prime * ugly_nums[idx + 1], prime, idx + 1))
            i += 1
        return ugly_nums[-1]


print Solution().nthSuperUglyNumber(12, [2, 3, 5])
print Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
