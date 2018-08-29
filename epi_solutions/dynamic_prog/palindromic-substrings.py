class Solution(object):
    def get_substrings_at_i_centre(self, i, s):
        start = i - 1
        end = i + 1
        palindromes = [(i, i)]
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            palindromes.append((start, end))
            start -= 1
            end += 1

        start = i
        end = i + 1
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            palindromes.append((start, end))
            start -= 1
            end += 1
        return palindromes

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [[0] * len(s) for _ in s]
        for i in range(len(s)):
            palindromes_i = self.get_substrings_at_i_centre(i, s)
            for p in palindromes_i:
                start, end = p
                dp[start][end] = 1
            # print s[i], i, palindromes_i, dp
        return sum(map(lambda x: sum(x), dp))


print Solution().countSubstrings('aaa')
print Solution().countSubstrings('abc')
