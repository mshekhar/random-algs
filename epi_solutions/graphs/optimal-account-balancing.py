import collections
import heapq


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """

        person_debt = collections.Counter()
        res = 0
        for (x, y, z) in transactions:
            person_debt[x] += z
            person_debt[y] -= z

        negative_heap = []
        positive_heap = []

        for person, debt in person_debt.iteritems():
            if debt < 0:
                heapq.heappush(negative_heap, debt)
            elif debt > 0:
                heapq.heappush(positive_heap, -1 * debt)

        print sorted(person_debt.items(), key=lambda x: x[1])

        while len(negative_heap) > 0:
            print negative_heap
            print positive_heap
            print '\n'

            max_positive = -1 * heapq.heappop(positive_heap)
            max_negative = heapq.heappop(negative_heap)
            res += 1
            if abs(max_positive) == abs(max_negative):
                continue
            elif abs(max_positive) > abs(max_negative):
                heapq.heappush(positive_heap, -1 * (abs(max_positive) - abs(max_negative)))
            else:
                heapq.heappush(negative_heap, -1 * (abs(max_negative) - abs(max_positive)))

        return res


# print Solution().minTransfers([[0, 1, 10], [2, 0, 5]])
# print Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]])
print Solution().minTransfers([[10, 11, 6], [12, 13, 7], [14, 15, 2], [14, 16, 2], [14, 17, 2], [14, 18, 2]])
