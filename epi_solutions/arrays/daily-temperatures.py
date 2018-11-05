class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        res = [0] * len(T)
        stack = []
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res


print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print Solution().dailyTemperatures([])
print Solution().dailyTemperatures([50])
