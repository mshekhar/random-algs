class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if not i and not j:
                    dp[i][j] = 0
                elif not i:
                    dp[i][j] = dp[i][j - 1] + ord(s2[j - 1])
                elif not j:
                    dp[i][j] = dp[i - 1][j] + ord(s1[i - 1])
                else:
                    both_del = dp[i - 1][j - 1]
                    if s1[i - 1] != s2[j - 1]:
                        both_del += ord(s2[j - 1]) + ord(s1[i - 1])
                    dp[i][j] = min(both_del,
                                   dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))
        # print dp
        return dp[-1][-1]


print Solution().minimumDeleteSum("sea", "eat")
