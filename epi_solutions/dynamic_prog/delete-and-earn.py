class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_val = max(nums)
        dp = [0] * (max_val + 1)

        for i in nums:
            dp[i] += i

        del_dp = [dp[0], max(dp[0], dp[1])]
        for c, i in enumerate(xrange(2, len(dp))):
            if dp[i]:
                del_dp.append(max(del_dp[i - 2] + dp[i], del_dp[i - 1]))
            else:
                del_dp.append(del_dp[i - 1])
        # print dp
        # print del_dp
        return max(del_dp)


print Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6])
