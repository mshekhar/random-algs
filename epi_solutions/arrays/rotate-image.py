class Solution(object):
    def get_matrix_size(self, matrix):
        try:
            m = len(matrix)
            n = len(matrix[0])
            if m < 1 or n < 1:
                return None, None
        except IndexError:
            return None, None
        return m, n

    def matrix_up_down(self, matrix):
        n = len(matrix)
        start = 0
        end = n - 1

        while start < end:
            for i in range(n):
                matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
            start += 1
            end -= 1

    def transpose(self, matrix):
        n = len(matrix)
        row_col = 0
        while row_col < n:
            for i in range(row_col + 1, n):
                # print 'exchange ', row_col, i, 'to', i, row_col, n
                matrix[row_col][i], matrix[i][row_col] = matrix[i][row_col], matrix[row_col][i]
            row_col += 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) < 1:
            return
        self.matrix_up_down(matrix)
        # print '\n'
        # for i in matrix:
        #     print i
        # print '\n'
        self.transpose(matrix)


def solve(matrix):
    print '\n'
    for i in matrix:
        print i
    Solution().rotate(matrix)
    for i in matrix:
        print i


solve([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
solve([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])
solve([])
solve([[1]])
