class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 1
        max_ele = None

        for i in arr:
            if max_ele is None:
                max_ele = i
            if i > max_ele:
                max_ele = i
                chunks += 1
