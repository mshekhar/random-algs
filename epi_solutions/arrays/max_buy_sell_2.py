class Solution(object):
    def get_max_buy_sell_ending_at_idx(self, prices):
        sol_ending_at_idx = [0]
        min_so_far = prices[0]
        sol_so_far = 0
        for i in range(1, len(prices)):
            res = prices[i] - min_so_far
            if res > sol_so_far:
                sol_so_far = res

            if prices[i] < min_so_far:
                min_so_far = prices[i]

            sol_ending_at_idx.append(sol_so_far)
        return sol_ending_at_idx

    def get_max_buy_sell_starting_at_idx(self, prices):
        sol_starting_at_idx = [0]
        max_so_far = prices[-1]
        sol_so_far = 0
        for i in range(len(prices) - 1)[::-1]:
            res = max_so_far - prices[i]
            if res > sol_so_far:
                sol_so_far = res

            if prices[i] > max_so_far:
                max_so_far = prices[i]

            sol_starting_at_idx.insert(0, sol_so_far)
        return sol_starting_at_idx

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        max_ending_idx = self.get_max_buy_sell_ending_at_idx(prices)
        max_starting_idx = self.get_max_buy_sell_starting_at_idx(prices)
        sol = 0
        for i in range(len(prices) - 1):
            res = max_ending_idx[i] + max_starting_idx[i + 1]
            if res > sol:
                sol = res
        return max(sol, max_ending_idx[-1], max_starting_idx[-1])


print Solution().get_max_buy_sell_ending_at_idx([3, 3, 5, 0, 0, 3, 1, 4])
print Solution().get_max_buy_sell_starting_at_idx([3, 3, 5, 0, 0, 3, 1, 4])
print Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])

print Solution().get_max_buy_sell_ending_at_idx([1, 2, 3, 4, 5])
print Solution().get_max_buy_sell_starting_at_idx([1, 2, 3, 4, 5])
print Solution().maxProfit([1, 2, 3, 4, 5])
print Solution().maxProfit([7, 6, 4, 3, 1])
print Solution().maxProfit([1, 2])
