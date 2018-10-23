class GraphNode(object):
    def __init__(self, node_num):
        self.node_num = node_num
        self.num_neighbors = 0
        self.path_sum_neighbors = 0
        self.neighbors = []

    def __str__(self):
        return str(self.node_num) + '->' + ",".join(map(lambda x: str(x.node_num), self.neighbors))

    def __repr__(self):
        return str(self.node_num) + '->' + ",".join(map(lambda x: str(x.node_num), self.neighbors))


class Solution(object):
    def postorder(self, root, seen):
        seen.add(root.node_num)
        for nei in root.neighbors:
            if nei.node_num not in seen:
                self.postorder(nei, seen)
                root.num_neighbors += nei.num_neighbors + 1
                root.path_sum_neighbors += nei.path_sum_neighbors + nei.num_neighbors + 1

    def preorder(self, root, seen, parent_node_count, parent_sum, res):
        # print 'calling ', root.node_num, 'with ', parent_node_count, parent_sum
        seen.add(root.node_num)
        res[root.node_num] = root.path_sum_neighbors + parent_sum + parent_node_count
        for nei in root.neighbors:
            if nei.node_num not in seen:
                child_num_nodes = root.num_neighbors - (nei.num_neighbors + 1) + parent_node_count + 1
                child_path_sum = root.path_sum_neighbors + parent_sum + parent_node_count - \
                                 (nei.path_sum_neighbors + nei.num_neighbors + 1)
                self.preorder(nei, seen, child_num_nodes, child_path_sum, res)

    def construct_graph(self, N, edges):
        graph = {n: GraphNode(n) for n in range(N)}
        for edge in edges:
            gn1 = graph[edge[0]]
            gn2 = graph[edge[1]]

            gn1.neighbors.append(gn2)
            gn2.neighbors.append(gn1)

        return graph

    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not N:
            return []
        if not edges:
            return [0] * N
        graph = self.construct_graph(N, edges)
        # print graph
        self.postorder(graph[0], set())
        # for i in graph:
        #     print i, graph[i], graph[i].num_neighbors, graph[i].path_sum_neighbors
        res = [0] * N
        self.preorder(graph[0], set(), 0, 0, res)
        return res


print Solution().sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
