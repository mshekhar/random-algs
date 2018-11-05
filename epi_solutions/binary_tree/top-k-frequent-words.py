import collections
import heapq


class HeapNode(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __cmp__(self, other):
        if self.freq == other.freq:
            return -1 * cmp(self.word, other.word)
        return cmp(self.freq, other.freq)


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or k < 1:
            return []
        word_counter = collections.Counter(words)
        min_heap = []
        for word, count in word_counter.items():
            heapq.heappush(min_heap, HeapNode(word, count))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap).word)
        return res[::-1]


print Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
# h1 = HeapNode('abc', 2)
# h2 = HeapNode('xyz', 2)
# h3 = HeapNode('ab', 2)
