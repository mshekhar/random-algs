import heapq


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """

        max_fuel_heap = []
        c = 0
        sorted_stations = sorted([d, f] for d, f in stations)

        for i in sorted_stations:
            if i[0] <= startFuel:
                heapq.heappush(max_fuel_heap, -i[1])
                c += 1
            else:
                break
        res = 0
        while startFuel < target:
            if max_fuel_heap:
                startFuel += -heapq.heappop(max_fuel_heap)
                res += 1
                # print startFuel, res, c

                while c < len(sorted_stations) and sorted_stations[c][0] <= startFuel:
                    heapq.heappush(max_fuel_heap, -1 * sorted_stations[c][1])
                    c += 1
                # print startFuel, res, c, max_fuel_heap
            else:
                return -1
        return res


print Solution().minRefuelStops(target=1, startFuel=1, stations=[])
print Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]])
print Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]])
