class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # if not A:
        #     return 0
        range_tracker = [[None, None] for _ in A]

        stack = []
        i = 0
        while i < len(A):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            range_tracker[i][0] = stack[-1] + 1 if stack else 0
            stack.append(i)
            # print 'min in stack ', i, A[i], range_tracker[i][0], stack
            i += 1

        stack = []
        i = len(A) - 1
        while i > -1:
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            range_tracker[i][1] = stack[-1] - 1 if stack else len(A) - 1
            stack.append(i)
            # print 'min in stack ', i, A[i], range_tracker[i][1], stack
            i -= 1

        # print range_tracker
        # print A
        res = sum(map(lambda x: (x[1][1] - x[0] + 1) * (x[0] - x[1][0] + 1) * A[x[0]], enumerate(range_tracker)))
        # print res
        return res % (10 ** 9 + 7)


print Solution().sumSubarrayMins([3, 1, 2, 4])
print Solution().sumSubarrayMins([59, 91])
