class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s

        frequency = [0] * 26
        pos = 0

        for i in range(len(s)):
            frequency[ord(s[i]) - ord('a')] += 1

        for i in range(len(s)):
            if ord(s[i]) < ord(s[pos]):
                pos = i
            frequency[ord(s[i]) - ord('a')] -= 1
            if not frequency[ord(s[i]) - ord('a')]:
                break
        new_s = "".join(filter(lambda x: x != s[pos], s[pos + 1:]))
        # print 'resp ', s[pos], pos + 1
        return s[pos] + self.removeDuplicateLetters(new_s)


print Solution().removeDuplicateLetters("bbacd")
print Solution().removeDuplicateLetters("abcacb")
print Solution().removeDuplicateLetters("bcabc")
print Solution().removeDuplicateLetters("cbacdcbc")
