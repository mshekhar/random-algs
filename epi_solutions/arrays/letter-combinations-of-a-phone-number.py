class Solution(object):
    digit_char = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def helper(self, digits, start, curr_str, res):
        if start == len(digits):
            res.append("".join(curr_str))
            return
        for next_char in self.digit_char[int(digits[start])]:
            curr_str.append(next_char)
            self.helper(digits, start + 1, curr_str, res)
            curr_str.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        res = []
        if digits:
            self.helper(digits, 0, [], res)
        return res


print Solution().letterCombinations("23")
print Solution().letterCombinations("33")
print Solution().letterCombinations("")
