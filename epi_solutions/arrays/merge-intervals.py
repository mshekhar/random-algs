# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def create_interval_arr(cls, intervals):
        arr = []
        for i in intervals:
            arr.append(Interval(s=i[0], e=i[1]))
        return arr

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        res = []
        intervals.sort(key=lambda x: x.start)
        i = 1
        active_interval = intervals[0]
        while i < len(intervals):
            if active_interval.end >= intervals[i].start:
                active_interval.end = max(active_interval.end, intervals[i].end)
            else:
                res.append(active_interval)
                active_interval = intervals[i]
            i += 1
        if active_interval:
            res.append(active_interval)
        return res


print Solution().merge(Interval.create_interval_arr([[1, 3], [2, 6], [8, 10], [15, 18]]))
print Solution().merge(Interval.create_interval_arr([[1, 4], [4, 5]]))
