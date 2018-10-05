class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        try:
            m = len(matrix)
            n = len(matrix[0])
            if m < 1 or n < 1:
                return
        except IndexError:
            return
        # print m, n
        row0_zero = False
        col0_zero = False

        for i in xrange(m):
            if matrix[i][0] == 0:
                col0_zero = True
            for j in xrange(n):
                if matrix[0][j] == 0:
                    row0_zero = True
                if matrix[i][j] == 0:
                    matrix[i][0] = None
                    matrix[0][j] = None

        # print '\n'
        # for i in matrix:
        #     print i
        # print row0_zero, col0_zero

        for i in xrange(m):
            if matrix[i][0] is None:
                if i == 0 and not row0_zero:
                    continue
                for j in xrange(n):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0

        # print '\n'
        # for i in matrix:
        #     print i

        for j in xrange(n):
            if matrix[0][j] is None:
                if j == 0 and not col0_zero:
                    continue
                for i in xrange(m):
                    if matrix[i][j] is not None:
                        matrix[i][j] = 0

        # print '\n'
        # for i in matrix:
        #     print i

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

    def print_res(self, mtx):
        for i in mtx:
            print i
        self.setZeroes(mtx)
        print '\n'
        for i in mtx:
            print i
        print '\n'


Solution().print_res([[1, 1, 1], [0, 1, 2]])

Solution().print_res([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
])

Solution().print_res([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])
