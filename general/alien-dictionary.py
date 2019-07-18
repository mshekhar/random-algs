import collections
from Queue import Queue


class Solution(object):
    def construct_graph(self, words):
        graph = {}
        i = 0
        while i < len(words):
            word_1 = words[i]
            i += 1
            j = i
            while j < len(words):
                word_2 = words[j]
                j += 1

                k = 0
                flag = False
                while k < len(word_1) or k < len(word_2):
                    if k < len(word_1) and word_1[k] not in graph:
                        graph[word_1[k]] = set()
                    if k < len(word_2) and word_2[k] not in graph:
                        graph[word_2[k]] = set()
                    if not flag and k < len(word_1) and k < len(word_2) and word_1[k] != word_2[k]:
                        graph[word_1[k]].add(word_2[k])
                        flag = True
                    k += 1
        return graph

    def topological_sort(self, graph):
        in_degrees = collections.Counter()

        for i in graph:
            for j in graph[i]:
                in_degrees[j] += 1
        queue = Queue()
        for i in graph:
            if in_degrees[i] == 0:
                queue.put(i)

        topological_order = []
        while queue.qsize() > 0:
            node = queue.get()
            topological_order.append(node)
            for i in graph[node]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.put(i)
        return topological_order

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            return words[0]
        graph = self.construct_graph(words)
        topological_sort = self.topological_sort(graph)
        if len(graph) == len(topological_sort):
            return "".join(topological_sort)
        return ""


print Solution().alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
])
print Solution().alienOrder([
    "z",
    "x"
])
print Solution().alienOrder([
    "z",
    "x",
    "z"
]
)
print Solution().alienOrder([
    "a"
])
print Solution().alienOrder(["abcdef", "dasdas"])
print Solution().alienOrder(["ad", "xy"])
print Solution().alienOrder(["ad", "adertyseqwewq", "xy"])
