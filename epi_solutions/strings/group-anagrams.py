class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for s in strs:
            res.setdefault("".join(sorted(s)), []).append(s)
        return res.values()


print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print Solution().groupAnagrams(["eat", "tea"])
print Solution().groupAnagrams(["eat"])
print Solution().groupAnagrams([])
