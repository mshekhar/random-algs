def ClosestXDestinations(numDestinations, allocations, numDeliveries):
    if numDeliveries > numDestinations or not allocations:
        return []
    print allocations
    return sorted(allocations, key=lambda x: x[0] ** 2 + x[1] ** 2)[:numDeliveries]


print ClosestXDestinations(3, [[1, 2], [3, 4], [1, -1]], 2)
print ClosestXDestinations(3, [[1, -3], [1, 2], [3, 4]], 1)
# print ClosestXDestinations(3, [[1, 2], [3, 4], [1, -1]], -1)
print ClosestXDestinations(6, [[3, 6], [2, 4], [5, 3], [2, 7], [1, 8], [7, 9]], 3)
