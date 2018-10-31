# http://www.zrzahid.com/the-%e2%80%a9maximum%e2%80%a9-gap%e2%80%a9-problem-%e2%80%a9pigeonhole-%e2%80%a9principle%e2%80%a9/
import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        arr_max = float('-inf')
        arr_min = float('inf')
        bucket_max = []
        bucket_min = []
        for i in nums:
            arr_max = max(arr_max, i)
            arr_min = min(arr_min, i)
            bucket_max.append(float('-inf'))
            bucket_min.append(float('inf'))

        bucket_delta = (arr_max - arr_min) * 1.0 / (len(nums) - 1)
        for i in nums:
            if i == arr_max or i == arr_min:
                continue
            idx = int(math.floor((i - arr_min) / bucket_delta))
            bucket_max[idx] = max(bucket_max[idx], i)
            bucket_min[idx] = min(bucket_min[idx], i)

        prev = arr_min
        max_gap = float('-inf')
        for i in range(len(bucket_min)):
            if bucket_min[i] == float('inf'):
                continue
            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]

        return max(max_gap, arr_max - prev)


print Solution().maximumGap([1, 2, 3, 4, 5, 8, 9])
print Solution().maximumGap([5, 1, 8, 9, 999999, 99999])
print Solution().maximumGap([5])
print Solution().maximumGap([5, 2])
