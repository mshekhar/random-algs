class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        freq_t = {}
        h_t = {}
        for i in t:
            if i not in freq_t:
                freq_t[i] = 0
            freq_t[i] += 1
            h_t[i] = 0

        c = 0
        start = 0
        end = 0
        solution_str = None
        while end < len(s):
            if s[end] in h_t:
                if h_t[s[end]] < freq_t[s[end]]:
                    c += 1
                h_t[s[end]] += 1
            # print s[end], h_t, freq_t, c
            while c == len(t):
                if s[start] in h_t:
                    h_t[s[start]] -= 1
                    if h_t[s[start]] < freq_t[s[start]]:
                        # print start, end, s[start], h_t
                        substr = s[start:end + 1]
                        if solution_str is None:
                            solution_str = substr
                        elif len(substr) < len(solution_str):
                            solution_str = substr

                        c -= 1
                start += 1
            end += 1
        return solution_str if solution_str else ""


print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("this is a test string", "tist")
print Solution().minWindow("geeksforgeeks", "ork")
