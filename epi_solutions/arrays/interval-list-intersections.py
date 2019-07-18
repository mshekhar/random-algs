class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []
        iter_a = 0
        iter_b = 0

        while iter_a < len(A) and iter_b < len(B):
            if B[iter_b][0] > A[iter_a][1]:
                iter_a += 1
            elif A[iter_a][0] > B[iter_b][1]:
                iter_b += 1
            else:
                res.append([max(A[iter_a][0], B[iter_b][0]), min(A[iter_a][1], B[iter_b][1])])
                if B[iter_b][1] >= A[iter_a][1]:
                    iter_a += 1
                else:
                    iter_b += 1
        return res


print Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
