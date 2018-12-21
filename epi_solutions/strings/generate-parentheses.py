class Solution(object):
    def helper(self, bracket_open_counter, bracket_closed_counter, curr_str, res):
        if bracket_open_counter == 0 and bracket_closed_counter == 0:
            res.append("".join(curr_str))
            return

        if bracket_open_counter > bracket_closed_counter or bracket_open_counter < 0 or bracket_closed_counter < 0:
            return

        curr_str.append('(')
        self.helper(bracket_open_counter - 1, bracket_closed_counter, curr_str, res)
        curr_str.pop()

        curr_str.append(')')
        self.helper(bracket_open_counter, bracket_closed_counter - 1, curr_str, res)
        curr_str.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        bracket_open_counter = n
        bracket_closed_counter = n
        res = []

        if n > 0:
            self.helper(bracket_open_counter, bracket_closed_counter, [], res)
        return res


print Solution().generateParenthesis(3)
print Solution().generateParenthesis(1)
