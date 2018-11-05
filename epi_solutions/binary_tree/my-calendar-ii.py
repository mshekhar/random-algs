# Definition for a binary tree node.
class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

    @classmethod
    def runner(cls, input, expected):
        obj = MyCalendarTwo()
        for c, i in enumerate(input):
            print i, expected[c], obj.book(*i)


null = None
true = True
false = False

MyCalendarTwo.runner([[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
                     [true, true, true, false, true, true])

# MyCalendarTwo.runner([[24, 40], [43, 50], [27, 43], [5, 21], [30, 40],
#                       [14, 29], [3, 19], [3, 14], [25, 39], [6, 19]],
#                      [true, true, true, true, false, false, true, false, false, false])
