class Solution(object):
    def helper(self, price, special, needs, dp):
        if tuple(needs) in dp:
            return dp[tuple(needs)]
        price_without_offer = sum([i * needs[c] for c, i in enumerate(price)])
        res = price_without_offer
        for s in special:
            new_needs = []
            can_apply_offer = True
            for c, n in enumerate(needs):
                if n - s[c] < 0:
                    can_apply_offer = False
                    break
                new_needs.append(n - s[c])
            if can_apply_offer:
                res = min(res, s[-1] + self.helper(price, special, new_needs, dp))
        dp[tuple(needs)] = res
        return res

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = {}
        res = self.helper(price, special, needs, dp)
        # print dp
        return res


print Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1])
print Solution().shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2])
