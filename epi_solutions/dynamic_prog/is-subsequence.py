class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        idx = 0
        for i in s:
            idx = t.find(i, idx)
            if idx == -1:
                return False
            idx += 1
        return True


print Solution().isSubsequence("b", "c")
print Solution().isSubsequence("axc", "ahbgdc")
