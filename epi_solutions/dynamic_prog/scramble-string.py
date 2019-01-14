class Solution(object):
    def helper(self, s1, s2):
        # print 'helper started', s1, s2
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True
        for i in xrange(1, len(s1)):
            if self.helper(s1[:i], s2[:i]) and self.helper(s1[i:], s2[i:]) or \
                    self.helper(s1[:i], s2[-i:]) and self.helper(s1[i:], s2[:-i]):
                # print 'helper finished', s1, s2
                return True
        # print 'helper finished', s1, s2
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.helper(s1.lower(), s2.lower())


# print Solution().isScramble("abc", "bca")
print Solution().isScramble("abcd", "bcda")
