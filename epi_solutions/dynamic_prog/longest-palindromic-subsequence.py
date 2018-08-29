class Solution(object):
    def helper(self, s, st, end, dp):
        if dp[st][end] is not None:
            return dp[st][end]
        if st > end:
            return 0
        if st == end:
            return 1

        if s[st] == s[end]:
            dp[st][end] = self.helper(s, st + 1, end - 1, dp) + 2
        else:
            dp[st][end] = max(self.helper(s, st + 1, end, dp), self.helper(s, st, end - 1, dp))

        return dp[st][end]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [[None for _ in range(len(s))] for _ in range(len(s))]

        return self.helper(s, 0, len(s) - 1, dp)


print Solution().longestPalindromeSubseq("GEEKSFORGEEKS")
print Solution().longestPalindromeSubseq("bbbab")
print Solution().longestPalindromeSubseq("cbbd")
