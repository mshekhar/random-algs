from heapq import heappush, heappop


class HeapObject(object):
    def __init__(self, src, dst, price, hops):
        self.src = src
        self.dst = dst
        self.price = price
        self.hops = hops

    def __cmp__(self, other):
        return cmp(self.price, other.price)

    def __str__(self):
        return str(self.src) + "_" + str(self.dst) + "_" + str(self.price)

    def __repr__(self):
        return str(self.src) + "_" + str(self.dst) + "_" + str(self.price)


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph = {}
        for i in flights:
            s, d, p = i
            if s not in graph:
                graph[s] = []
            graph[s].append((d, p))

        if src not in graph:
            return -1

        heap = []

        # print graph
        for neighbor in graph[src]:
            heappush(heap, HeapObject(src=src, dst=neighbor[0], price=neighbor[1], hops=0))
        while heap:
            # print heap
            heap_obj = heappop(heap)

            if heap_obj.dst == dst:
                return heap_obj.price

            if heap_obj.hops + 1 > K:
                continue

            for neighbor in graph[heap_obj.dst]:
                heappush(heap, HeapObject(src=heap_obj.dst, dst=neighbor[0],
                                          price=heap_obj.price + neighbor[1],
                                          hops=heap_obj.hops + 1))
        return -1


print Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1)
