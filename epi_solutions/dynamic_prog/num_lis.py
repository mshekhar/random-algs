class LISObject(object):
    def __init__(self, val=None, uniq_seq=None):
        self.val = val or float('-inf')
        self.uniq_seq = uniq_seq or 1

    def __str__(self):
        return str(self.val) + "_" + str(self.uniq_seq)

    def __repr__(self):
        return str(self.val) + "_" + str(self.uniq_seq)


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = []
        for _ in nums:
            lis.append(LISObject(val=1))
        for c in range(1, len(nums)):
            for i in range(0, c):
                # print nums[c], nums[i], lis[c], lis[i], lis
                if nums[c] > nums[i]:
                    if lis[c].val < lis[i].val + 1:
                        lis[c].val = lis[i].val + 1
                        lis[c].uniq_seq = lis[i].uniq_seq
                    elif lis[c].val == lis[i].val + 1:
                        lis[c].uniq_seq += lis[i].uniq_seq
        max_lis = float('-inf')
        uniq_lis = 0

        for i in lis:
            max_lis = max(i.val, max_lis)

        for i in lis:
            if i.val == max_lis:
                uniq_lis += i.uniq_seq

        # print lis, max_lis, uniq_lis
        return uniq_lis


print Solution().findNumberOfLIS([1, 3, 5, 4, 7, 6])
print Solution().findNumberOfLIS([1, 3, 5, 4, 7])
print Solution().findNumberOfLIS([2, 2, 2, 2, 2])
print Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2])
# 1 2 3 4 7
# 1 2 4 5 7
# 1 2 3 5 7
