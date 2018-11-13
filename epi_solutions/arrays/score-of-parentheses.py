class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                curr = 0
                while stack and isinstance(stack[-1], (int, long)):
                    curr += stack.pop()
                stack.pop()
                if curr == 0:
                    stack.append(1)
                else:
                    stack.append(2 * curr)
            # print s, stack
        return sum(stack)


print Solution().scoreOfParentheses("")
print Solution().scoreOfParentheses("()")
print Solution().scoreOfParentheses("(())")
print Solution().scoreOfParentheses("()()")
print Solution().scoreOfParentheses("(()(()))")
