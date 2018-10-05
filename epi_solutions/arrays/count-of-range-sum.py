# TODO Segment Tree
class Solution(object):
    def merge(self, nums, lo, mid, hi, res, lower, upper):
        nums1 = nums[lo:mid]
        nums2 = nums[mid:hi]
        merge = []
        c1 = 0
        c2 = 0
        p1 = 0
        p2 = 0
        # print 'merge ', nums1, nums2, res
        while c1 < len(nums1):
            while p2 < len(nums2) and nums2[p2] - nums1[c1] <= upper:
                p2 += 1
            while p1 < len(nums2) and nums2[p1] - nums1[c1] < lower:
                p1 += 1
            res += p2 - p1
            while c2 < len(nums2) and nums1[c1] >= nums2[c2]:
                merge.append(nums2[c2])
                c2 += 1
            merge.append(nums1[c1])
            c1 += 1
        while c2 < len(nums2):
            merge.append(nums2[c2])
            c2 += 1
        return res, merge

    def sort(self, nums, lo, hi, lower, upper):
        if hi <= lo:
            return 0
        if hi - lo == 1:
            return 0
        mid = lo + (hi - lo) / 2
        # print lo, mid, hi
        res = self.sort(nums, lo, mid, lower, upper) + self.sort(nums, mid, hi, lower, upper)
        res, merge = self.merge(nums, lo, mid, hi, res, lower, upper)
        nums[lo:hi] = merge
        # print 'merged ', merge, nums, res
        return res

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
        # print 'arr ', prefix_sum
        res = self.sort(prefix_sum, 0, len(prefix_sum), lower, upper)
        return res


print Solution().countRangeSum([-2, 5, -1], -2, 2)
