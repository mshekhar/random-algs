from operator import add, sub, mul, div


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        oper_map = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
        }
        stack = []
        for i in tokens:
            if len(i) == 1 and 42 <= ord(i) <= 47:
                val_1 = stack.pop()
                val_2 = stack.pop()
                # print 'applying ', oper_map[i], val_2, val_1, int(oper_map[i](val_2, val_1))
                # casting to float because of negative number division problem in python
                stack.append(int(oper_map[i](float(val_2), float(val_1))))
            else:
                stack.append(int(i))
        return stack


print Solution().evalRPN(["2", "1", "+", "3", "*"])
print Solution().evalRPN(["4", "13", "5", "/", "+"])
print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
