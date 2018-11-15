class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        seen = set()
        repeated = set()
        i = 0
        while i < len(s) - 9:
            new_str = s[i:i + 10]
            i += 1
            if new_str in seen:
                repeated.add(new_str)
            else:
                seen.add(new_str)
        return list(repeated)
