# Definition for a point.
from fractions import gcd


class Point(object):
    MAX_SLOPE = float('inf')

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def get_slope_between_point(self, p2):
        try:
            return (self.y - p2.y) * 1.0 / (self.x - p2.x)
        except ZeroDivisionError:
            return float('inf')

    def get_y_intercept(self, slope):
        return self.y - (slope * self.x)

    def get_slope_key(self, p2):
        x = self.x - p2.x
        if x is 0:
            return self.MAX_SLOPE
        y = self.y - p2.y
        if y is 0:
            return 0
        gc = gcd(x, y)
        return Point(a=x / gc, b=y / gc)

    def get_hash_key(self, p2):
        slope = self.get_slope_between_point(p2)
        y_intercept = self.get_y_intercept(slope)
        point = self.get_slope_key(p2)

        if slope == 0:
            return str(y_intercept)
        elif slope == self.MAX_SLOPE:
            return 'inf'
        else:
            return str(y_intercept) + '_' + str(point.x) + '_' + str(point.y)


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        max_val = 0
        for i in range(len(points)):
            p1 = points[i]
            same = 1
            h = {}
            point = Point(p1.x, p1.y)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                point_2 = Point(p2.x, p2.y)
                if point_2.x == point.x and point_2.y == point.y:
                    same += 1
                else:
                    slope_key = point.get_hash_key(point_2)
                    if slope_key not in h:
                        h[slope_key] = 0
                    h[slope_key] += 1
            if same > max_val:
                max_val = same
            for k, v in h.iteritems():
                if v + same > max_val:
                    max_val = v + same
        return max_val

    @classmethod
    def test_method(cls, arr):
        max_p = []
        for a in arr:
            max_p.append(Point(a[0], a[1]))
        return Solution().maxPoints(max_p)


# print Solution().test_method([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
# print Solution().test_method([[1, 1], [2, 2], [3, 3]])
# print Solution().test_method([[0, 0], [1, 1], [0, 0]])
# print Solution().test_method([[0, 0]])
# print Solution().test_method(
#     [[0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4], [3, 4], [-2, 4], [-1, 4], [0, -5], [0, -8], [-2, -1],
#      [0, -11], [0, -9]])
# print Point(4,, 1).get_slope_key(Point(1, 1))
