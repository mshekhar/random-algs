class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = []
        right_max = []
        water_trapped = 0
        height_rev = height[::-1]
        max_ele = -1
        for c, i in enumerate(height):
            if i > max_ele:
                max_ele = i
            left_max.append(max_ele)

        max_ele = -1
        for c, i in enumerate(height_rev):
            if i > max_ele:
                max_ele = i
            right_max.append(max_ele)
        right_max = right_max[::-1]
        for c, i in enumerate(height):
            water_trapped += min(left_max[c], right_max[c]) - i
        return water_trapped


print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
