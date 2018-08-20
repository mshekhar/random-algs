class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.sum_mtx = self.init_sum_mtx()

    def get_mtx_val(self, row, col, mtx):
        if row < 0 or col < 0:
            return 0
        try:
            return mtx[row][col]
        except IndexError:
            return 0

    def init_sum_mtx(self):
        sum_mtx = [[0] * len(c) for c in self.matrix]
        for row, row_arr in enumerate(sum_mtx):
            for col, _ in enumerate(row_arr):
                # print row, col
                sum_mtx[row][col] -= self.get_mtx_val(row - 1, col - 1, sum_mtx)
                sum_mtx[row][col] += self.get_mtx_val(row - 1, col, sum_mtx)
                sum_mtx[row][col] += self.get_mtx_val(row, col - 1, sum_mtx)
                sum_mtx[row][col] += self.get_mtx_val(row, col, self.matrix)

        return sum_mtx

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.get_mtx_val(row2, col2, self.sum_mtx) + \
               self.get_mtx_val(row1 - 1, col1 - 1, self.sum_mtx) - \
               self.get_mtx_val(row1 - 1, col2, self.sum_mtx) - \
               self.get_mtx_val(row2, col1 - 1, self.sum_mtx)


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print obj.sum_mtx
print obj.sumRegion(2, 1, 4, 3), 8
print obj.sumRegion(1, 1, 2, 2), 11
print obj.sumRegion(1, 2, 2, 4), 12
