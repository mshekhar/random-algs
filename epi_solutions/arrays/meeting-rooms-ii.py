import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: x[0])
        # print intervals

        min_heap_end_times = []
        number_of_meeting_rooms = 0
        for start, end in intervals:
            while min_heap_end_times and start >= min_heap_end_times[0]:
                heapq.heappop(min_heap_end_times)
            heapq.heappush(min_heap_end_times, end)
            number_of_meeting_rooms = max(number_of_meeting_rooms, len(min_heap_end_times))

        return number_of_meeting_rooms


# print Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
# print Solution().minMeetingRooms([[7, 10], [2, 4]])
# print Solution().minMeetingRooms([[13, 15], [1, 13]])
print Solution().minMeetingRooms([[6, 17], [8, 9], [11, 12], [6, 9]])
