class Solution(object):
    def generate_odd_palindrome(self, s, idx):
        l_idx = idx - 1
        r_idx = idx + 1
        p_str = [s[idx]]
        while l_idx >= 0 and r_idx < len(s):
            if s[l_idx] != s[r_idx]:
                break
            p_str.insert(0, s[l_idx])
            p_str.append(s[r_idx])
            l_idx -= 1
            r_idx += 1
        return "".join(p_str)

    def generate_even_palindrome(self, s, idx):
        l_idx = idx
        r_idx = idx + 1
        p_str = []
        # print 'gen even ', l_idx, r_idx, idx, s[idx]
        while l_idx >= 0 and r_idx < len(s):
            if s[l_idx] != s[r_idx]:
                break
            # print 'adding even ', s[l_idx], s[r_idx]
            p_str.insert(0, s[l_idx])
            p_str.append(s[r_idx])
            l_idx -= 1
            r_idx += 1
        return "".join(p_str)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_p_str = ''
        for i in range(len(s)):
            odd_p_str = self.generate_odd_palindrome(s, i)
            even_p_str = self.generate_even_palindrome(s, i)
            if len(odd_p_str) > len(max_p_str):
                max_p_str = odd_p_str
            if len(even_p_str) > len(max_p_str):
                max_p_str = even_p_str
        return max_p_str


print Solution().longestPalindrome("bb")
# print Solution().longestPalindrome("cbbd")

import itertools
for c, i in enumerate(itertools.permutations(range(1, 21))):
    if sum(i[:-1]) > 300:
        print i
    if c%100 == 0:
        print c