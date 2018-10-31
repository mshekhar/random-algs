class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        A.sort()
        pos_b = [(c, i) for c, i in enumerate(B)]
        pos_b.sort(key=lambda x: x[1])
        lo_a = 0
        hi_a = len(A) - 1
        res = [None for _ in A]

        counter = 0
        while counter < len(A):
            counter += 1
            idx, val = pos_b.pop()
            if A[hi_a] > val:
                res[idx] = A[hi_a]
                hi_a -= 1
            else:
                res[idx] = A[lo_a]
                lo_a += 1
        return res


print Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11])
print Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11])
