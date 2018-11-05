import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        sum_map = collections.Counter()
        res = 0
        for i in A:
            for j in B:
                sum_map[i + j] += 1

        for i in C:
            for j in D:
                res += sum_map.get(-1 * (i + j), 0)
        return res
