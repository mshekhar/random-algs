class Solution(object):
    def merge(self, nums, lo, mid, hi, res):
        nums1 = nums[lo:mid]
        nums2 = nums[mid:hi]
        merge = []
        c1 = 0
        c2 = 0
        p = 0
        # print 'merging ', nums1, nums2, res
        while c1 < len(nums1):
            while p < len(nums2) and nums1[c1] > 2 * nums2[p]:
                p += 1
            res += p
            while c2 < len(nums2) and nums1[c1] >= nums2[c2]:
                merge.append(nums2[c2])
                c2 += 1
            merge.append(nums1[c1])
            c1 += 1
        while c2 < len(nums2):
            merge.append(nums2[c2])
            c2 += 1
        return res, merge

    def sort(self, nums, lo, hi):
        if hi <= lo:
            return 0
        if hi - lo == 1:
            return 0
        mid = lo + (hi - lo) / 2
        # print lo, mid, hi
        res = self.sort(nums, lo, mid) + self.sort(nums, mid, hi)
        res, merge = self.merge(nums, lo, mid, hi, res)
        nums[lo:hi] = merge
        # print 'merged ', merge, nums, res
        return res

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.sort(nums, 0, len(nums))


print Solution().reversePairs([1, 3, 2, 3, 1])
print Solution().reversePairs([2, 4, 3, 5, 1])
