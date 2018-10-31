class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minimum_till_now = float('inf')
        max_profit_till_now = 0
        for price in prices:
            max_profit_till_now = max(max_profit_till_now, price - minimum_till_now)
            minimum_till_now = min(minimum_till_now, price)
        return max_profit_till_now


print Solution().maxProfit([7, 1, 5, 3, 6, 4])
print Solution().maxProfit([7, 6, 4, 3, 1])
print Solution().maxProfit([7])
print Solution().maxProfit([7, 6])
print Solution().maxProfit([6, 7])
