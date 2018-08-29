class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        # 0 top
        # 1 left
        # 2 down
        # 3 right
        # min all
        axis_aligned_1_dp = [[[1, 1, 1, 1] for _ in xrange(N)] for _ in xrange(N)]
        mines_set = set()
        for mine in mines:
            mines_set.add((mine[0], mine[1]))

        for i in range(N):
            for j in range(N):
                if (i, j) not in mines_set:
                    if i:
                        axis_aligned_1_dp[i][j][0] = 1 + axis_aligned_1_dp[i - 1][j][0]

                    if j:
                        axis_aligned_1_dp[i][j][1] = 1 + axis_aligned_1_dp[i][j - 1][1]
                else:
                    axis_aligned_1_dp[i][j] = [0, 0, 0, 0]

        # for i in axis_aligned_1_dp:
        #     print i
        # print '\n'
        sol = 0
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if (i, j) not in mines_set:
                    if i != N - 1:
                        axis_aligned_1_dp[i][j][2] = 1 + axis_aligned_1_dp[i + 1][j][2]

                    if j != N - 1:
                        axis_aligned_1_dp[i][j][3] = 1 + axis_aligned_1_dp[i][j + 1][3]

                    sol = max(sol, min(axis_aligned_1_dp[i][j]))
                else:
                    axis_aligned_1_dp[i][j] = [0, 0, 0, 0]

        # for i in axis_aligned_1_dp:
        #     print i
        return sol


print Solution().orderOfLargestPlusSign(5, [[4, 2]])
print Solution().orderOfLargestPlusSign(2, [])
print Solution().orderOfLargestPlusSign(1, [[0, 0]])
