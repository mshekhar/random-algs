class Solution(object):
    def helper(self, boxes, st, end, k, dp):
        if st > end:
            return 0
        if dp[st][end][k] and dp[st][end][k] > 0:
            return dp[st][end][k]

        while st + 1 < len(boxes) and boxes[st] == boxes[st + 1]:
            st += 1
            k += 1
        res = (k + 1) * (k + 1) + self.helper(boxes, st + 1, end, 0, dp)
        print st, end, k, boxes[st], res

        for m in xrange(st + 1, end + 1):
            if boxes[st] == boxes[m]:
                res = max(res, self.helper(boxes, st + 1, m - 1, 0, dp) + self.helper(boxes, m, end, k + 1, dp))

        dp[st][end][k] = res
        return res

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        dp = [[[None for _ in xrange(len(boxes))] for _ in xrange(len(boxes))] for _ in xrange(len(boxes))]
        return self.helper(boxes, 0, len(boxes) - 1, 0, dp)


# print Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])

print Solution().removeBoxes(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
