import heapq


class BuildingNode(object):
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height

    def __cmp__(self, other):
        return cmp(-self.height, -other.height)

    def __str__(self):
        return str(self.start) + "_" + str(self.end) + "_" + str(self.height)

    def __repr__(self):
        return str(self)


class Solution(object):
    def add_to_res(self, res, t, height):
        if res and res[-1][1] == height:
            return
        if res and res[-1][0] == t and height > res[-1][1]:
            res.pop()
        res.append([t, height])

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        buildings_obj = map(lambda x: BuildingNode(*x), buildings)
        for building in buildings:
            buildings_obj.append(BuildingNode(start=building[1], end=float('inf'), height=0))
        buildings_obj.sort(key=lambda x: x.start)
        # print buildings_obj
        res = []
        max_heap = []
        max_height = float('-inf')
        i = 0
        while i < len(buildings_obj):

            if buildings_obj[i].height > max_height:
                max_height = buildings_obj[i].height
                self.add_to_res(res, buildings_obj[i].start, max_height)

            heapq.heappush(max_heap, buildings_obj[i])

            if buildings_obj[i].height == 0 and max_heap and max_heap[0].end <= buildings_obj[i].start:
                while max_heap and max_heap[0].end <= buildings_obj[i].start:
                    _ = heapq.heappop(max_heap)
                if max_heap:
                    max_height = max_heap[0].height
                else:
                    max_height = 0
                self.add_to_res(res, buildings_obj[i].start, max_height)

            # print max_heap

            i += 1
        return res

    @classmethod
    def runner(cls, buildings, expected):
        res = Solution().getSkyline(buildings)
        if not res == expected:
            print '\n'
            print res, expected, res == expected
            print '\n'
        else:
            print res, expected, res == expected


Solution.runner([], [])
Solution.runner([[0, 2147483647, 2147483647]], [[0, 2147483647], [2147483647, 0]])
Solution.runner([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
                [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
Solution.runner([[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]],
                [[3, 8], [7, 7], [8, 6], [9, 5], [10, 4], [11, 3], [12, 2], [13, 1], [14, 0]])
Solution.runner([[2, 4, 7], [2, 4, 5], [2, 4, 6]], [[2, 7], [4, 0]])
Solution.runner([[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]],
                [[0, 7], [5, 12], [10, 7], [15, 12], [20, 7], [25, 0]])
Solution.runner([[0, 2, 3], [2, 4, 3], [4, 6, 3]], [[0, 3], [6, 0]])
Solution.runner([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])
Solution.runner([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]])
Solution.runner([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
                [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
Solution.runner([[1, 5, 11], [2, 7, 6], [3, 9, 13], [12, 16, 7], [14, 25, 3], [19, 22, 18], [23, 29, 13], [24, 28, 4]],
                [[1, 11], [3, 13], [9, 0], [12, 7], [16, 3], [19, 18], [22, 3], [23, 13], [29, 0]])
