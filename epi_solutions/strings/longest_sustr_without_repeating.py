class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        h = {}
        max_substr_len = 0
        curr_start = 0
        for c, i in enumerate(s):
            if i not in h:
                h[i] = c
            else:
                tmp_start = h[i] + 1
                for j in range(curr_start, tmp_start):
                    h.pop(s[j])
                curr_start = tmp_start
                h[i] = c
            max_substr_len = max(max_substr_len, c - curr_start + 1)

        return max_substr_len


print Solution().lengthOfLongestSubstring("abcabcbb"), 3
print Solution().lengthOfLongestSubstring("bbbbb"), 1
print Solution().lengthOfLongestSubstring("pwwkew"), 3
print Solution().lengthOfLongestSubstring("abcbacbb"), 3
