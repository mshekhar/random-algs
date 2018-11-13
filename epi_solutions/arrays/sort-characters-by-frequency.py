import collections


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        res = []
        for i, freq in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            res.extend([i] * freq)
        return "".join(res)
