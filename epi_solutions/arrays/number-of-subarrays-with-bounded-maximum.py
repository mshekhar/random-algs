class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        res = 0
        i = 0
        j = 0

        valid_subarray_len = 0
        while i < len(A):
            if L <= A[i] <= R:
                valid_subarray_len = i - j + 1
                res += valid_subarray_len
            elif A[i] < L:
                res += valid_subarray_len
            else:
                valid_subarray_len = 0
                j = i + 1
            # print 'ele ', A[i], valid_subarray_len, res
            i += 1

        return res


print Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)
print Solution().numSubarrayBoundedMax([2, 1, 4, 1, 2, 1, 3, 1, 4, 3], 2, 3)
print Solution().numSubarrayBoundedMax([2, 1, 4, 1, 2, 1, 3], 2, 3)
