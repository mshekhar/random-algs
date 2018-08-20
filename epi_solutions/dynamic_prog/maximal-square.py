class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = []
        for c_i, i in enumerate(matrix):
            if c_i == 0:
                dp.append(map(lambda x: int(x), i))
                continue
            dp.append([])
            for c_j, j in enumerate(i):
                if c_j == 0:
                    dp[-1].append(int(j))
                else:
                    if j == '1':
                        # print dp, c_i, c_j
                        dp[-1].append(min(dp[c_i][c_j - 1], dp[c_i - 1][c_j], dp[c_i - 1][c_j - 1]) + 1)
                    else:
                        dp[-1].append(0)

        max_val = float('-inf')
        for c_i, i in enumerate(dp):
            for c_j, j in enumerate(i):
                max_val = max(j, max_val)
        return max_val * max_val if max_val != float('-inf') else 0


print Solution().maximalSquare([["1", "0", "1", "0", "0"],
                                ["1", "0", "1", "1", "1"],
                                ["1", "1", "1", "1", "1"],
                                ["1", "0", "0", "1", "0"]])
print Solution().maximalSquare([])
