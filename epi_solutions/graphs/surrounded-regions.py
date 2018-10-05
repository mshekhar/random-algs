from Queue import Queue


class Solution(object):
    def get_mtx_val(self, row, col, mtx):
        if row < 0 or col < 0:
            return -1
        try:
            return mtx[row][col]
        except IndexError:
            return -1

    def set_mtx_val(self, row, col, mtx):
        if row < 0 or col < 0:
            return -1
        try:
            mtx[row][col] = 'X'
        except IndexError:
            return -1

    def get_neighbors(self, row, col):
        return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        try:
            m = len(board)
            n = len(board[0])
            if m < 1 or n < 1:
                return
        except IndexError:
            return
        # print m, n
        visited = set()
        bfs_queue = Queue()

        for i in (0, m - 1):
            for j in xrange(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    # print 'first ', i, j, board[i][j]
                    visited.add((i, j))
                    bfs_queue.put((i, j))

        for i in xrange(m):
            for j in (0, n - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    # print 'second ', i, j, board[i][j]
                    visited.add((i, j))
                    bfs_queue.put((i, j))

        while bfs_queue.qsize() > 0:
            i, j = bfs_queue.get()
            for new_i, new_j in self.get_neighbors(i, j):
                if self.get_mtx_val(new_i, new_j, board) == 'O' and (new_i, new_j) not in visited:
                    # print 'third ', new_i, new_j, board[new_i][new_j]
                    visited.add((new_i, new_j))
                    bfs_queue.put((new_i, new_j))

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O' and not (i, j) in visited:
                    self.set_mtx_val(i, j, board)


def run(board):
    for i in board:
        print i
    print '\n'
    Solution().solve(board)
    for i in board:
        print i


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'X', 'X']
]
run(board)
