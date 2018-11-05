class Solution(object):
    def swap(self, next_ele, partner, row, idx_map):
        partner_idx = idx_map[partner]
        next_ele_idx = idx_map[next_ele]
        idx_map[partner] = next_ele_idx
        idx_map[next_ele] = partner_idx

        row[partner_idx], row[next_ele_idx] = row[next_ele_idx], row[partner_idx]

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        idx_map = {k: c for c, k in enumerate(row)}
        swaps = 0

        for i in xrange(0, len(row) - 1, 2):
            partner = row[i] - 1 if row[i] % 2 else row[i] + 1
            if row[i + 1] != partner:
                self.swap(row[i + 1], partner, row, idx_map)
                swaps += 1

        return swaps


print Solution().minSwapsCouples([0, 2, 1, 3])
print Solution().minSwapsCouples([3, 2, 0, 1])
print Solution().minSwapsCouples([])
