class Solution(object):
    def merge(self, nums, lo, mid, hi, dp):
        nums1 = nums[lo:mid]
        nums2 = nums[mid:hi]
        c1 = 0
        c2 = 0
        k = lo
        # print 'merge ', nums1, nums2
        inversions = 0
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1][1] <= nums2[c2][1]:
                dp[nums1[c1]] += inversions
                nums[k] = nums1[c1]
                c1 += 1
            else:
                nums[k] = nums2[c2]
                # print 'smaller ', nums1[c1][1], nums2[c2][1], dp[nums1[c1]]
                inversions += 1
                c2 += 1
            k += 1

        if c1 < len(nums1):
            while c1 < len(nums1):
                nums[k] = nums1[c1]
                dp[nums1[c1]] += inversions
                k += 1
                c1 += 1

        while c2 < len(nums2):
            nums[k] = nums2[c2]
            k += 1
            c2 += 1

    def sort(self, nums, lo, hi, dp):
        if hi <= lo:
            return
        if hi - lo == 1:
            return
        mid = lo + (hi - lo) / 2
        # print lo, mid, hi
        self.sort(nums, lo, mid, dp)
        self.sort(nums, mid, hi, dp)
        self.merge(nums, lo, mid, hi, dp)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = {(c, k): 0 for c, k in enumerate(nums)}
        tmp_nums = [(c, k) for c, k in enumerate(nums)]
        self.sort(tmp_nums, 0, len(tmp_nums), dp)
        res = [None] * len(nums)
        for i in tmp_nums:
            res[i[0]] = dp[i]
        # print nums
        # print res
        # print tmp_nums
        return res


print Solution().countSmaller([5, 2, 6, 1])
print Solution().countSmaller([12, 11, 13, 5, 6, 7])
print Solution().countSmaller([0, 5, 3, 2, 2])
print Solution().countSmaller([0, 5, 3, 2, 1, 2])
print Solution().countSmaller([0])
print Solution().countSmaller([-2, -5, -45])
