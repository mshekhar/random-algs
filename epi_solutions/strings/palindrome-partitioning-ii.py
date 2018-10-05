class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        p_dp = [[False for _ in s] for _ in s]
        for i in xrange(len(s)):
            p_dp[i][i] = True
        cuts = [i for i in xrange(len(s))]
        is_palindrome = lambda x, y: s[x] == s[y] and (y - x - 1 < 2 or p_dp[x + 1][y - 1])

        for l in xrange(2, len(s) + 1):
            i = 0
            j = l - 1
            while j < len(s):
                if is_palindrome(i, j):
                    p_dp[i][j] = True
                    # cuts[j] = 0 if not i - 1 >= 0 else min(cuts[j], cuts[i - 1] + 1)
                else:
                    p_dp[i][j] = False
                    # cuts[j] = min(cuts[j - 1] + 1, cuts[j])
                i += 1
                j += 1
        # for i in p_dp:
        #     j = i
        #     print i

        for i in xrange(len(s)):
            if p_dp[0][i]:
                cuts[i] = 0
            else:
                for j in xrange(i):
                    if p_dp[j + 1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)
            # print i, cuts
        # print cuts
        # print p_dp
        return cuts[-1]


print Solution().minCut('aab')
print Solution().minCut('a')
print Solution().minCut('ababbbab')
print Solution().minCut('babbbab')
print Solution().minCut('ababbbabbababa')
print Solution().minCut('ababbbabbababa')
