# TODO suffix array radix

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        if not A or not B:
            return 0
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        max_len = 0
        for i in range(len(A) + 1):
            for j in range(len(B) + 1):
                if not i or not j:
                    dp[i][j] = 0
                    continue
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_len = max(max_len, dp[i][j])
        return max_len


print Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
print Solution().findLength([3, 2, 1, 4, 7], [1, 2, 3, 2, 1])
print Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])
print Solution().findLength([0, 1, 1, 1, 0], [1, 1, 1, 1, 1])
print Solution().findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1])
