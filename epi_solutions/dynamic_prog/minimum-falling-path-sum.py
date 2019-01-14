class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        try:
            m = len(A)
            n = len(A[0])
            if m < 1 or n < 1:
                return 0
        except IndexError:
            return 0
        col_range = range(n)
        aux_mtx = A[-1][:]
        for i in xrange(-2, -(m + 1), -1):
            aux_cpy = []
            for j in col_range:
                min_range = [aux_mtx[j]]
                if j - 1 >= 0:
                    min_range.append(aux_mtx[j - 1])
                if j + 1 < n:
                    min_range.append(aux_mtx[j + 1])
                aux_cpy.append(A[i][j] + min(min_range))
            aux_mtx = aux_cpy
        return min(aux_mtx)


print Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print Solution().minFallingPathSum([[1]])
print Solution().minFallingPathSum([])
print Solution().minFallingPathSum([[]])
print Solution().minFallingPathSum([[1, 2, -1]])
