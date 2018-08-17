class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = []
        sum_all = sum(nums[0:k])
        dp.append(sum_all)
        for i in range(k, len(nums)):
            # print sum_all, nums[i - k], nums[k], i
            sum_all = sum_all - nums[i - k] + nums[i]
            dp.append(sum_all)

        left = [0] * len(dp)
        best = 0
        for i in range(len(dp)):
            if dp[i] > dp[best]:
                best = i
            left[i] = best

        right = [0] * len(dp)
        best = len(dp) - 1
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] >= dp[best]:
                best = i
            right[i] = best

        # print dp
        # print left
        # print right

        ans = None
        for j in xrange(k, len(dp) - k):
            i, m = left[j - k], right[j + k]
            if ans is None or (dp[i] + dp[j] + dp[m] >
                               dp[ans[0]] + dp[ans[1]] + dp[ans[2]]):
                ans = i, j, k
        return ans


print Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)

# try:
#     print Solution().maxSumOfThreeSubarrays2([1, 2, 1, 2, 6, 7, 5, 1], 2)
# except:
#     import time
#
#     time.sleep(0.5)
#     print e
