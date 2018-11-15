import collections


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_area = float('inf')
        row_elements = collections.defaultdict(set)
        col_elements = collections.defaultdict(set)
        points_set = set()
        for p in points:
            row_elements[p[0]].add(p[1])
            col_elements[p[1]].add(p[0])
            points_set.add(tuple(p))

        for p in points:
            for row_num in col_elements[p[1]]:
                if row_num == p[0]:
                    continue
                # p1 = [row_num, p[1]]
                for col_num in row_elements[row_num]:
                    if col_num == p[1]:
                        continue
                    # p2 = [row_num, col_num]
                    # p3 = [p[0], col_num]
                    if (p[0], col_num) in points_set:
                        # print p, [row_num, p[1]], [row_num, col_num], [p[0], col_num], abs(row_num - p[0]) * abs(
                        #     col_num - p[1])
                        min_area = min(min_area, abs(row_num - p[0]) * abs(col_num - p[1]))
        return min_area if min_area != float('inf') else 0


print Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
print Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]])
print Solution().minAreaRect([[2, 2], [4, 4]])
print Solution().minAreaRect([[0, 1], [1, 3], [3, 3], [4, 4], [1, 4], [2, 3], [1, 0], [3, 4]])

# import numpy as np
# from matplotlib import pyplot as plt
#
# data = np.array([[0, 1], [1, 3], [3, 3], [4, 4], [1, 4], [2, 3], [1, 0], [3, 4]])
# x, y = data.T
# plt.scatter(x, y)
# plt.show()
