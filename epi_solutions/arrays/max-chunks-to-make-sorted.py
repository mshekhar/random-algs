class Solution(object):
    def get_max_till_now(self, A):
        max_till_now = []
        max_ele = float('-inf')
        for i in A:
            max_ele = max(max_ele, i)
            max_till_now.append(max_ele)
        return max_till_now

    def get_min_after_now(self, A):
        min_after_now = []
        min_ele = float('inf')
        for i in xrange(len(A) - 1, -1, -1):
            min_after_now.append(min_ele)
            min_ele = min(min_ele, A[i])
        return min_after_now[::-1]

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if not arr:
            return 0
        max_till_now = self.get_max_till_now(arr)
        min_after_now = self.get_min_after_now(arr)
        # print max_till_now
        # print min_after_now
        chunks = 0
        for i in xrange(len(arr)):
            if max_till_now[i] <= min_after_now[i]:
                chunks += 1
            # else:
            #     if ele_count:
            #         chunks += 1
            #         ele_count = 0
            #     ele_count += 1
            # print i, arr[i], chunks, ele_count, max_till_now[i], min_after_now[i]
        return chunks


print Solution().maxChunksToSorted([1, 0, 2, 3, 4])
print Solution().maxChunksToSorted([4, 3, 2, 1, 0])
