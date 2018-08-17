class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        return self.compute_skyline(buildings)
        # sorted_skyline = sorted(skylines, key=lambda x: x[0])
        # return sorted_skyline

    def append_to_result(self, skylines, item, last_ele=False):
        if skylines and item[1] == skylines[-1][1]:
            if last_ele:
                skylines[-1] = item
            return skylines
        if skylines and item[0] == skylines[-1][0]:
            if item[1] >= skylines[-1][1]:
                skylines[-1] = item
            return skylines

        skylines.append(item)
        return skylines

    def merge_2_skyline_inputs(self, sk1, sk2):
        skylines = []

        small_start = sk1 if sk1[0] <= sk2[0] else sk2
        start_other = sk1 if sk1[0] > sk2[0] else sk2
        if small_start == start_other:
            skylines = self.append_to_result(skylines, [small_start[0], max(small_start[2], start_other[2])])
        else:
            skylines = self.append_to_result(skylines, [small_start[0], small_start[2]])
            if start_other[0] > small_start[1]:
                skylines = self.append_to_result(skylines, [small_start[1], 0])
            if start_other[2] > small_start[2]:
                skylines = self.append_to_result(skylines, [start_other[0], start_other[2]])
            elif start_other[1] > small_start[1]:
                skylines = self.append_to_result(skylines, [small_start[1], start_other[2]])

            if start_other[1] < small_start[1]:
                skylines = self.append_to_result(skylines, [start_other[1], small_start[2]])
            skylines = self.append_to_result(skylines, [max(small_start[1], start_other[1]), 0], last_ele=True)
        return skylines

    # def merge_2_skyline_inputs(self, sk1, sk2):
    #     skylines = []
    #     small_start = sk1 if sk1[0] <= sk2[0] else sk2
    #     start_other = sk1 if sk1[0] > sk2[0] else sk2
    #     if small_start == start_other:
    #         skylines.append([small_start[0], max(small_start[2], start_other[2])])
    #     else:
    #         skylines.append([small_start[0], small_start[2]])
    #         if start_other[0] > small_start[1]:
    #             skylines.append([small_start[1] + 1, 0])
    #         if start_other[2] > small_start[2]:
    #             skylines.append([start_other[0], start_other[2]])
    #         elif start_other[1] > small_start[1]:
    #             skylines.append([small_start[1] + 1, start_other[2]])
    #
    #         if start_other[1] < small_start[1]:
    #             skylines.append([start_other[1] + 1, small_start[2]])
    #         skylines.append([max(small_start[1], start_other[1]) + 1, 0])
    #     return skylines

    def compute_skyline(self, skyline):
        if len(skyline) <= 2:
            if len(skyline) < 2:
                sk = skyline[0]
                return [[sk[0], sk[2]], [sk[1], 0]]
            return self.merge_2_skyline_inputs(skyline[0], skyline[1])
        mid = len(skyline) / 2
        sk1 = skyline[:mid]
        sk2 = skyline[mid:]
        skyline_1 = self.compute_skyline(sk1)
        skyline_2 = self.compute_skyline(sk2)
        return self.merge_skylines(skyline_1, skyline_2)

    def merge_skylines(self, skyline_1, skyline_2):
        print skyline_1, '****', skyline_2
        sk1_idx = 0
        sk2_idx = 0
        sk1_h = 0
        sk2_h = 0
        result = []

        while True:
            if sk1_idx == len(skyline_1) and sk2_idx == len(skyline_2):
                break
            elif sk1_idx == len(skyline_1):
                for item in skyline_2[sk2_idx:]:
                    result = self.append_to_result(result, item)
                break
            elif sk2_idx == len(skyline_2):
                for item in skyline_1[sk1_idx:]:
                    result = self.append_to_result(result, item)
                break

            if skyline_1[sk1_idx][0] == skyline_2[sk2_idx][0]:
                if skyline_1[sk1_idx][1] >= skyline_2[sk2_idx][1]:
                    sk1_h = skyline_1[sk1_idx][1]
                    result = self.append_to_result(result, [skyline_1[sk1_idx][0], max(sk1_h, sk2_h)])
                    sk1_idx += 1
                    sk2_idx += 1
                else:
                    sk2_h = skyline_2[sk2_idx][1]
                    result = self.append_to_result(result, [skyline_2[sk2_idx][0], max(sk1_h, sk2_h)])
                    sk2_idx += 1
                    sk1_idx += 1
            elif skyline_1[sk1_idx][0] < skyline_2[sk2_idx][0]:
                sk1_h = skyline_1[sk1_idx][1]
                result = self.append_to_result(result, [skyline_1[sk1_idx][0], max(sk1_h, sk2_h)])
                sk1_idx += 1
            else:
                sk2_h = skyline_2[sk2_idx][1]
                result = self.append_to_result(result, [skyline_2[sk2_idx][0], max(sk1_h, sk2_h)])
                sk2_idx += 1
        result = self.append_to_result(result, [max(skyline_1[-1][0], skyline_2[-1][0]), 0], last_ele=True)
        print 'result', result
        return result

    # Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])


# import pdb
#
# pdb.set_trace()
# print Solution().merge_2_skyline_inputs([15, 20, 10], [19, 24, 8])
# print Solution().merge_skylines([(1, 11), (3, 13), (9, 0), (12, 7), (16, 0)],
#                                 [(14, 3), (19, 18), (22, 3), (23, 13), (29, 0)])
#
print Solution().getSkyline([[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5],
                             [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]])
# print Solution().merge_2_skyline_inputs([0, 2, 3], [2, 4, 3])
# print Solution().merge_2_skyline_inputs([2, 4, 3], [4, 6, 3])
# print Solution().getSkyline([[2, 4, 7], [2, 4, 5], [2, 4, 6]])
# print Solution().getSkyline([[0, 5, 7], [5, 10, 7], [5, 10, 12],
#                              [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]])
# print Solution().getSkyline([[0, 2, 3], [2, 4, 3], [4, 6, 3]])
# print Solution().getSkyline([[0, 2, 3], [2, 5, 3]])
# print Solution().getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
# print Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
# print Solution().getSkyline([[1, 5, 11], [2, 7, 6], [3, 9, 13],
#                              [12, 16, 7], [14, 25, 3], [19, 22, 18], [23, 29, 13], [24, 28, 4]])
# [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
