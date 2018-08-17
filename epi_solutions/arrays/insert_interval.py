#
# def get_intervals(self, intervals, newInterval, idx):
#     right_intervals = []
#     left_intervals = []
#     min_left = newInterval[0]
#     max_right = newInterval[1]
#     for i in range(idx, len(intervals)):
#         if newInterval[1] >= intervals[i][1]:
#             continue
#         if newInterval[1] == intervals[i][0]:
#             max_right = intervals[i][1]
#             continue
#         if newInterval[1] > intervals[i][0]:
#             if newInterval[1] + 1 == intervals[i][1]:
#                 max_right = intervals[i][1]
#                 continue
#             else:
#                 if intervals[i][0] < newInterval[0]:
#                     min_left = min(min_left, intervals[i][0])
#                 right_intervals.append([newInterval[1] + 1, intervals[i][1]])
#                 continue
#         right_intervals.append(intervals[i])
#
#     for i in range(0, idx)[::-1]:
#         if newInterval[0] <= intervals[i][0]:
#             continue
#         if newInterval[0] == intervals[i][1]:
#             min_left = intervals[i][0]
#             continue
#         if newInterval[0] < intervals[i][1]:
#             if newInterval[0] + 1 == intervals[i][1]:
#                 min_left = intervals[i][0]
#                 continue
#             else:
#                 # print 'left insert ', newInterval, intervals[i], [intervals[i][0],
#                 #                                                   newInterval[0] - 1], left_intervals, i
#                 left_intervals.insert(0, [intervals[i][0], newInterval[0] - 1])
#                 continue
#         left_intervals.insert(0, intervals[i])
#     return min_left, max_right, left_intervals, right_intervals
#
#
# def insert(self, intervals, newInterval):
#     """
#     :type intervals: List[Interval]
#     :type newInterval: Interval
#     :rtype: List[Interval]
#     """
#     # print intervals, intervals[0].__dict__, intervals[0].__module__, intervals[0].start, intervals[0].end
#     if not intervals:
#         return [newInterval]
#     idx = self.bisect_right(intervals, newInterval[1])
#     min_left, max_right, left_intervals, right_intervals = self.get_intervals(intervals, newInterval, idx)
#     # print idx, len(intervals), newInterval, intervals[idx]
#     return left_intervals + [[min_left, max_right]] + right_intervals


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def bisect_left(self, a, x, lo=0, hi=None):
        """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e < x, and all e in
        a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
        insert just before the leftmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
        """

        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid].start < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def bisect_right(self, a, x, lo=0, hi=None):
        """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e <= x, and all e in
        a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
        insert just after the rightmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
        """

        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid].end:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def print_smoothen_res(self, left_interval, right_interval, newInterval):
        print 'print_smoothen_res'
        l = []
        for i in left_interval:
            l.append([i.start, i.end])
        print 'left ', l
        r = []
        for i in right_interval:
            r.append([i.start, i.end])
        print 'right ', r
        print 'new_interval ', newInterval.start, newInterval.end

    def smoothen_res(self, left_interval, right_interval, newInterval):
        # self.print_smoothen_res(left_interval, right_interval, newInterval)
        if left_interval:
            end_interval = left_interval[-1]
            if end_interval.end < newInterval.start:
                pass
            else:
                left_interval = left_interval[:-1]
                newInterval.start = end_interval.start
        if right_interval:
            start_interval = right_interval[0]
            if start_interval.start > newInterval.end:
                pass
            else:
                right_interval = right_interval[1:]
                newInterval.end = start_interval.end
        return left_interval + [newInterval] + right_interval

    def insert(self, intervals, newInterval):
        left_idx = self.bisect_left(intervals, newInterval.start)
        right_idx = self.bisect_right(intervals, newInterval.end)

        left_interval = []
        right_interval = []
        if left_idx > 0:
            left_interval = intervals[:left_idx]
        if right_idx < len(intervals):
            right_interval = intervals[right_idx:]

        return self.smoothen_res(left_interval, right_interval, newInterval)

    def test_arr(self, intervals, newInterval):
        inp = []
        for i in intervals:
            inp.append(Interval(s=i[0], e=i[1]))
        merged_res = self.insert(inp, Interval(s=newInterval[0], e=newInterval[1]))
        res = []
        for i in merged_res:
            res.append([i.start, i.end])
        return res


print Solution().test_arr([[1, 2], [3, 5], [4, 6], [6, 7], [8, 10], [12, 16]], [4, 8])
print Solution().test_arr([[1, 3], [6, 9]], [2, 5])
print Solution().test_arr([[1, 3]], [2, 5])
print Solution().test_arr([[0, 4]], [2, 2])
print Solution().test_arr([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
