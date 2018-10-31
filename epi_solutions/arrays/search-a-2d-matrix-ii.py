class Solution(object):
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
        r = 0
        c = n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
