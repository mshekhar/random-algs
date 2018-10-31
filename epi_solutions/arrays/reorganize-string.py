import heapq


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        sorted_str = sorted(S)
        max_heap = []
        word_freq = [0 for _ in xrange(26)]
        for i in sorted_str:
            word_freq[ord(i) - ord('a')] += 1

        for i in xrange(26):
            if word_freq[i]:
                heapq.heappush(max_heap, (-word_freq[i], str(unichr(ord('a') + i))))
        res = []
        staged_ele = None
        while max_heap:
            w_freq, char = heapq.heappop(max_heap)
            res.append(char)
            if staged_ele:
                heapq.heappush(max_heap, staged_ele)
                staged_ele = None
            if w_freq + 1 < 0:
                staged_ele = (w_freq + 1, char)
        if staged_ele is not None:
            res = []
        return "".join(res)


print Solution().reorganizeString('baa')
print Solution().reorganizeString('aaab')
