class Solution(object):
    def get_matrix_ele(self, m, n, matrix, pos):
        row = pos / n
        col = pos % n
        return matrix[row][col]

    def bsearch(self, m, n, matrix, target):
        lo = 0
        hi = m * n - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if self.get_matrix_ele(m, n, matrix, mid) < target:
                lo = mid + 1
            else:
                hi = mid
        if lo >= m * n or self.get_matrix_ele(m, n, matrix, lo) != target:
            return None
        return lo

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            m = len(matrix)
            n = len(matrix[0])
            if m < 1 or n < 1:
                return False
        except IndexError:
            return False

        idx = self.bsearch(m, n, matrix, target)
        return idx is not None

    def runner(self, matrix):
        for i in matrix:
            for j in i:
                print j - 1, self.searchMatrix(matrix, j - 1)
                print j, self.searchMatrix(matrix, j)
                print j + 1, self.searchMatrix(matrix, j + 1)


print Solution().runner([
    [1, 3, 5, 7, 8],
    [10, 11, 16, 20, 21],
    [23, 30, 34, 50, 55]
])
