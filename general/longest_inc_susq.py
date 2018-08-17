from bisect import bisect_right


class Solution(object):
    def binary_search_find(self, a, x, lo=0, hi=None):
        hi = hi if hi is not None else len(a)
        pos = bisect_right(a, x, lo, hi)
        return pos

    def binary_lis(self, nums):
        lis = []
        for i in nums:
            pos = bisect_right(lis, i)
            # print 'processing ', i, lis, pos
            if len(lis) > 0 and pos > 0 and lis[pos - 1] == i:
                continue
            if pos == len(lis):
                lis.append(i)
            else:
                lis[pos] = i
        # print 'printing', lis
        return len(lis)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []

        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) // 2
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binary_lis(nums)


from general.data_provider import get_test_case

for test_case in get_test_case('data_provider/lis.tsv'):
    try:
        res = Solution().lengthOfLIS2(test_case['input'])
        print test_case['input'], test_case['result'], res

        assert res == test_case['result']
    except AssertionError:
        import time

        time.sleep(0.5)
        raise
