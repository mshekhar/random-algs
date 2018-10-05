import collections


class Solution(object):
    # TODO Tree ceil/floor solution
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        nums_k = collections.OrderedDict()
        for i in nums:
            key = i / t if t else i
            for m in (nums_k.get(key - 1), nums_k.get(key), nums_k.get(key + 1)):
                if m is not None and abs(i - m) <= t:
                    return True
            if len(nums_k) >= k:
                nums_k.popitem(last=False)
            nums_k[key] = i
        return False


print Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0)
print Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2)
print Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3)
