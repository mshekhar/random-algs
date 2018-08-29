class Solution(object):
    def isMoveLegal(self, r, c, N):
        return N > r >= 0 and N > c >= 0

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        valid_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        total_moves = 8 ** K
        dp = [[1 for _ in xrange(N)] for _ in xrange(N)]
        for _ in xrange(K):
            temp_dp = [[0 for _ in xrange(N)] for _ in xrange(N)]
            for i in xrange(N):
                for j in xrange(N):
                    for move in valid_moves:
                        new_row = i + move[0]
                        new_col = j - move[1]
                        if self.isMoveLegal(new_row, new_col, N):
                            # print ("changing " + str(i) + "_" + str(j) + "_" + str(new_row) + "_" + str(new_col) + "_" + str(temp_dp[i][j]) + "_" + str(dp[new_row][new_col]))
                            temp_dp[i][j] += dp[new_row][new_col]
            dp = temp_dp
        # print dp[r][c]
        # print total_moves
        return dp[r][c] * 1.0 / total_moves


print Solution().knightProbability(3, 2, 0, 0)
