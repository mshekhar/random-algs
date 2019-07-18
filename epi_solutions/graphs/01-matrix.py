from Queue import Queue


class Solution(object):
    def is_idx_valid(self, k1, k2, board):
        if k1 < 0 or k2 < 0:
            return False
        try:
            _ = board[k1][k2]
        except IndexError:
            return False
        return True

    def get_valid_neighbors(self, i, j, board):
        for k1, k2 in [(i - 1, j),
                       (i, j - 1),
                       (i, j + 1),
                       (i + 1, j)]:
            if self.is_idx_valid(k1, k2, board):
                yield k1, k2

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        queue = Queue()
        try:
            m = len(matrix)
            n = len(matrix[0])
            if not m or not n:
                return matrix
        except:
            return matrix

        result = [[-1 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    queue.put((i, j, 0))

        while queue.qsize() > 0:
            i, j, dist = queue.get()
            for k1, k2 in self.get_valid_neighbors(i, j, matrix):
                if result[k1][k2] == -1:
                    result[k1][k2] = dist + 1
                    queue.put((k1, k2, dist + 1))
        return result


print Solution().updateMatrix([[0, 0, 0],
                               [0, 1, 0],
                               [1, 1, 1]])
print Solution().updateMatrix([[0, 0, 0],
                               [0, 1, 0],
                               [0, 0, 0]])
