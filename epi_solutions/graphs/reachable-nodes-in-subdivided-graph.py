import heapq


class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """

        adjacency_list = {}
        visited = set()
        for i in edges:
            from_node, to_node, between_nodes = i

            if from_node not in adjacency_list:
                adjacency_list[from_node] = {}
            adjacency_list[from_node][to_node] = between_nodes

            if to_node not in adjacency_list:
                adjacency_list[to_node] = {}
            adjacency_list[to_node][from_node] = between_nodes

        max_heap = []
        heapq.heappush(max_heap, (M, 0))
        result = 0
        while max_heap:
            moves_left, from_node = heapq.heappop(max_heap)
            if from_node in visited:
                continue
            visited.add(from_node)
            result += 1
            for to_node in adjacency_list.get(from_node, {}):
                moves_req = adjacency_list[from_node][to_node] + 1
                if moves_left >= moves_req:
                    heapq.heappush(max_heap, (moves_left - moves_req, to_node))

                reach = min(moves_left, moves_req - 1)  # cost will only reach cost - 1 new nodes
                # old node will be counted at the start of new round
                result += reach
                adjacency_list[to_node][from_node] -= reach

        return result


print Solution().reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3)
print Solution().reachableNodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4)
