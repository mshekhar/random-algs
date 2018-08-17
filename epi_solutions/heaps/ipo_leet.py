import heapq


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        max_profit_heap = []
        c = 0
        cap_profits = sorted([c, p] for c, p in zip(Capital, Profits))

        for i in cap_profits:
            if i[0] <= W:
                heapq.heappush(max_profit_heap, -i[1])
                c += 1
            else:
                break

        while k > 0:
            if max_profit_heap:
                max_sum = -heapq.heappop(max_profit_heap)
                # print max_sum, W, c, max_profit_heap
                W += max_sum
                while c < len(cap_profits) and cap_profits[c][0] <= W:
                    heapq.heappush(max_profit_heap, -1 * cap_profits[c][1])
                    c += 1
            k -= 1

        return W


print Solution().findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1])
print Solution().findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[1, 1, 2])
print Solution().findMaximizedCapital(k=50, W=50, Profits=range(0, 50), Capital=range(0, 50))
print Solution().findMaximizedCapital(k=50000, W=50000, Profits=range(0, 50000), Capital=range(0, 50000))
