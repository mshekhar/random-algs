class Solution(object):
    def is_idx_valid(self, k1, k2, board):
        if k1 < 0 or k2 < 0:
            return False
        try:
            _ = board[k1][k2]
        except IndexError:
            return False
        return True

    def get_live_neighbor_count(self, i, j, board):
        count = 0
        for k1, k2 in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                       (i, j - 1), (i, j + 1),
                       (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            if self.is_idx_valid(k1, k2, board):
                # print k1, k2, board[k1][k2] & 1
                count += board[k1][k2] & 1
        return count

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        try:
            m = len(board)
            n = len(board[0])
            if m < 1 or n < 1:
                return
        except IndexError:
            return

        for i in xrange(m):
            for j in xrange(n):
                count = self.get_live_neighbor_count(i, j, board)
                # print i, j, count
                if board[i][j] & 1 == 0 and count == 3:
                    board[i][j] = 2
                elif board[i][j] & 1 == 1:
                    if count > 3 or count < 2:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1

    def runner(self, board):
        for i in board:
            print i
        print '\n'
        self.gameOfLife(board)
        for i in board:
            print i
        print '\n'


Solution().runner([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
])
