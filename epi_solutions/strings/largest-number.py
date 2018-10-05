class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = "".join(sorted(map(lambda x: str(x), nums), cmp=lambda x, y: cmp(x + y, y + x), reverse=True)).lstrip("0")
        return res if res else "0"


print Solution().largestNumber([3, 30, 34, 5, 9])
print Solution().largestNumber([10, 2])
print Solution().largestNumber([0, 0])
