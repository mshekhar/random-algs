from bisect import insort_right


class Solution(object):
    def get_median(self, arr):
        if len(arr) % 2:
            median = arr[len(arr) / 2]
        else:
            median = (arr[len(arr) / 2] + arr[(len(arr) / 2) - 1]) / 2.0
        return float(median)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not k:
            return []
        if k == 1:
            return map(lambda x: float(x), nums)
        res = []
        window = []

        for c, i in enumerate(nums):
            if len(window) == k:
                res.append(self.get_median(window))
                window.remove(nums[c - k])
            insort_right(window, i)
        res.append(self.get_median(window))
        return res


print Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 2)
