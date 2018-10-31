class Solution(object):
    def wordBreak(self, s, word_set):
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

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=lambda x: len(x))
        words_till_now = set()
        res = []
        for i in words:
            if not i:
                continue
            if self.wordBreak(i, words_till_now):
                res.append(i)
            words_till_now.add(i)
        return res


print Solution().findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog",
                                                  "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
