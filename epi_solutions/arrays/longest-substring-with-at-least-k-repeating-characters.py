class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k <= 0:
            return 0

        counter = [0] * 26
        for i in s:
            counter[ord(i) - ord('a')] += 1

        if min(filter(lambda x: x > 0, counter)) >= k:
            return len(s)

        start = 0
        end = 0
        max_len_str = 0
        while end < len(s):
            curr_counter = [0] * 26
            while end < len(s) and counter[ord(s[end]) - ord('a')] >= k:
                curr_counter[ord(s[end]) - ord('a')] += 1
                end += 1

            new_start = end + 1
            if min(filter(lambda x: x > 0, curr_counter)) >= k:
                max_len_str = max(max_len_str, end - start)
            else:
                pass

        return 0


# print Solution().longestSubstring(s="aaabb", k=3)
# print Solution().longestSubstring(s="a", k=1)
# print Solution().longestSubstring(s="", k=1)
# print Solution().longestSubstring(s="ababbc", k=2)
# print Solution().longestSubstring("weitong", 2)
import pdb

pdb.set_trace()
print Solution().longestSubstring("bbaaacbd", 3)
