class Solution(object):
    def __init__(self):
        self.last_k = []

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        for c, i in enumerate(nums):
            if not self.last_k:
                self.last_k.append(i)
            elif i > self.last_k[0]:
                self.last_k = []
                self.last_k.append(i)
            else:
                if len(self.last_k) >= k:
                    self.last_k = self.last_k[1:]
                    if not self.last_k:
                        self.last_k.append(i)
                    else:
                        max_ele = max(self.last_k)
                        if i > max_ele:
                            self.last_k = []
                            self.last_k.append(i)
                        else:
                            self.last_k.append(i)
                            max_ele_index = self.last_k.index(max_ele)
                            self.last_k = self.last_k[max_ele_index:]
                else:
                    self.last_k.append(i)

            if c + 1 >= k:
                result.append(self.last_k[0])
        return result


# print Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print Solution().maxSlidingWindow([7, 2, 4], 2)
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
