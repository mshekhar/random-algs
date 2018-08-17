class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        max_left = []
        min_right = []
        max_till_now = float('-inf')
        min_till_now = float('inf')
        for i in arr:
            max_till_now = max(i, max_till_now)
            max_left.append(max_till_now)

        for i in arr[::-1]:
            min_till_now = min(i, min_till_now)
            min_right.insert(0, min_till_now)

        for i in range(len(arr)):
            if i + 1 >= len(arr):
                break
            next_min = min_right[i + 1]
            # print min_right[i], max_left[i], arr[i], next_min, chunks
            if min_right[i] == max_left[i] == arr[i]:
                chunks += 1
            elif max_left[i] <= next_min:
                chunks += 1
        # print max_left
        # print min_right
        return chunks + 1


print Solution().maxChunksToSorted([2, 1, 3, 4, 4])
print Solution().maxChunksToSorted([5, 4, 3, 2, 1])
print Solution().maxChunksToSorted([1, 0, 1, 3, 2])
