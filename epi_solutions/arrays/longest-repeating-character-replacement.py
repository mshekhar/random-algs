class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for i in set(s):
            start = 0
            end = 0
            remaining_k = k
            for j in s:
                if j != i:
                    if remaining_k > 0:
                        remaining_k -= 1
                        end += 1
                    else:
                        while s[start] == i:
                            start += 1
                        start += 1
                        end += 1
                else:
                    end += 1
                # print chr(i), j, end, start, res, remaining_k
                res = max(end - start, res)
        return res


print Solution().characterReplacement("ABAB", 1)
print Solution().characterReplacement("ABAB", 0)
print Solution().characterReplacement("ABAB", 2)
print Solution().characterReplacement("ABAB", 4)
print Solution().characterReplacement("AABABBA", 1)
print Solution().characterReplacement("AABABBA", 0)
print Solution().characterReplacement("AABABBA", 2)
print Solution().characterReplacement("AABABBA", 3)
print Solution().characterReplacement("AABABBA", 4)
