import heapq


def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    # print noOfCurrentAgents, callsTimes
    callsTimes.sort(key=lambda x: x[0])
    min_heap = []
    peak_concurrent = 0
    for call in callsTimes:
        begin = call[0]
        end = call[1]
        while min_heap and begin > min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)
        peak_concurrent = max(peak_concurrent, len(min_heap))
    res = peak_concurrent - noOfCurrentAgents
    return 0 if res <= 0 else res


print howManyAgentsToAdd(1, [[1481122000, 1481122020], [1481122000, 1481122040], [1481122030, 1481122035]])
