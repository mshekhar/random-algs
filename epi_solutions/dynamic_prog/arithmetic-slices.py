class Solution(object):
    def count_number(self, n):
        if n < 3:
            return 0
        pos = ((n - 2) * n) + 1
        neg = (n * (n - 1)) / 2
        return pos - neg

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 3:
            return 0

        st_idx = 0
        end_idx = 1
        running_diff = []
        for i in range(1, len(A)):
            running_diff.append(A[i] - A[i - 1])

        # print running_diff
        r_diff = running_diff[0]
        sol = 0
        while end_idx < len(A) - 1:
            # print r_diff, running_diff[end_idx], st_idx, end_idx
            if running_diff[end_idx] == r_diff:
                end_idx += 1
                continue
            else:
                sol += self.count_number(end_idx - st_idx + 1)
                r_diff = running_diff[end_idx]
                st_idx = end_idx
                end_idx += 1
        sol += self.count_number(end_idx - st_idx + 1)
        return sol


print Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9])
print Solution().numberOfArithmeticSlices([7, 7, 7, 7])
print Solution().numberOfArithmeticSlices([3, -1, -5, -9])
print Solution().numberOfArithmeticSlices([1, 1, 2, 5, 7])
print Solution().numberOfArithmeticSlices([1, 2, 3, 4])
