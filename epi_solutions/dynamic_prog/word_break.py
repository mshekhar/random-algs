class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        word_set = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(s)):
            if not dp[i] and s[0:i + 1] in word_set:
                dp[i] = True

            if dp[i]:
                for j in range(i + 1, len(s)):
                    if not dp[j] and s[i + 1:j + 1] in word_set:
                        dp[j] = True

                if dp[-1]:
                    return True
        return False


print Solution().wordBreak('leetcode', ["leet", "code"])
print Solution().wordBreak('applepenapple', ["apple", "pen"])
print Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
