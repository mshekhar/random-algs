class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if not i and not j:
                    dp[i][j] = 0
                elif not i:
                    dp[i][j] = dp[i][j - 1] + 1
                elif not j:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]


print Solution().minDistance("geek", "gesek")
print Solution().minDistance("cat", "cut")
print Solution().minDistance("sunday", "saturday")
print Solution().minDistance("horse", "ros")
print Solution().minDistance("intention", "execution")
