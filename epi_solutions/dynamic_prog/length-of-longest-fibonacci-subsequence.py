import collections


class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        idx_map = {x: c for c, x in enumerate(A)}
        longest_pair = collections.defaultdict(lambda: 2)
        max_len = 0

        for c, i in enumerate(A):
            for j in xrange(c):
                k = idx_map.get(i - A[j])
                if k is not None and k < j:
                    longest_pair[(j, c)] = longest_pair[k, j] + 1
                    max_len = max(max_len, longest_pair[(j, c)])
        return max_len


print Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
print Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18])
print Solution().lenLongestFibSubseq([3, 4, 5, 6, 7, 8])
