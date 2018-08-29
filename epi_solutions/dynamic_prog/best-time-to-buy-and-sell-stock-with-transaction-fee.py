class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_so_far = prices[0]
        max_so_far = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_so_far:
                if max_so_far - min_so_far - fee > 0:
                    profit += max_so_far - min_so_far - fee
                min_so_far = prices[i]
                max_so_far = prices[i]
            elif max_so_far - prices[i] > fee:
                if max_so_far - min_so_far - fee > 0:
                    profit += max_so_far - min_so_far - fee
                    min_so_far = prices[i]
                    max_so_far = prices[i]
            elif prices[i] >= max_so_far:
                max_so_far = prices[i]
        if max_so_far - min_so_far - fee > 0:
            profit += max_so_far - min_so_far - fee
        return profit


print Solution().maxProfit([10, 1, 6, 3, 12], 2)
print Solution().maxProfit([1, 6, 3, 12], 2)
print Solution().maxProfit([1, 6], 2)
print Solution().maxProfit([1, 4, 3, 9], 2)
