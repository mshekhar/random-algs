class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) < 2:
            return len(pairs)
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        curr = sorted_pairs[0][1]
        max_len = 1
        for i in sorted_pairs:
            if i[0] > curr:
                curr = i[1]
                max_len += 1
        return max_len


print Solution().findLongestChain([[1, 2], [2, 3], [3, 4]])
