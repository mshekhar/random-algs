class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        char_idx_map = {}
        contribution_map = {}
        res = 0
        cur = 0
        for i, ch in enumerate(S):
            cur -= contribution_map.get(ch, 0)
            contribution_map[ch] = (i - (char_idx_map.get(ch, 0) - 1))
            cur += contribution_map[ch]
            char_idx_map[ch] = i + 1
            res += cur

        return res


print Solution().uniqueLetterString("ABCBD")
print Solution().uniqueLetterString("ABC")
print Solution().uniqueLetterString("ABA")
