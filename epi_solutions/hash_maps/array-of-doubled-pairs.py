import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        num_set = collections.Counter(A)

        for k in sorted(num_set, key=abs):
            if num_set[k] <= num_set[2 * k]:
                num_set[2 * k] -= num_set[k]
                continue
            return False
        return True


print Solution().canReorderDoubled([3, 1, 3, 6])
print Solution().canReorderDoubled([2, 1, 2, 6])
print Solution().canReorderDoubled([4, -2, 2, -4])
print Solution().canReorderDoubled([0, 0])
print Solution().canReorderDoubled([10, 20, 40, 80])
