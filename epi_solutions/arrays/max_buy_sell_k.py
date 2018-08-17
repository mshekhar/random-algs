class Solution(object):
    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sol = []
        max_profit = 0
        for i in range(k + 1):
            sol.append([0] * len(prices))

        for i in range(1, k + 1):
            diff = sol[i - 1][0] - prices[0]
            for j in range(1, len(prices)):
                sol[i][j] = max(sol[i][j - 1], diff + prices[j])
                diff = max(diff, sol[i - 1][j] - prices[j])
                max_profit = max(max_profit, sol[i][j])
        return max_profit

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sol = []
        max_profit = 0
        sol.append([0] * len(prices))
        for i in range(1, k + 1):
            diff = sol[0][0] - prices[0]
            sol.append([0] * len(prices))
            for j in range(1, len(prices)):
                sol[1][j] = max(sol[1][j - 1], diff + prices[j])
                diff = max(diff, sol[0][j] - prices[j])
                max_profit = max(max_profit, sol[1][j])
            sol = [sol[1]]
        return max_profit


print Solution().maxProfit(2, [10, 22, 5, 75, 65, 80]), 87
print Solution().maxProfit(3, [12, 14, 17, 10, 14, 13, 12, 15]), 12
print Solution().maxProfit(3, [100, 30, 15, 10, 8, 25, 80]), 72
print Solution().maxProfit(1, [90, 80, 70, 60, 50]), 0
print Solution().maxProfit(2, []), 0
