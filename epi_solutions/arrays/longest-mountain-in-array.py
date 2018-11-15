class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        longest_mountain = 0
        curr_mountain_start = -1
        curr_mountain_peak = -1
        curr_mountain_end = -1

        i = 1
        while i < len(A):
            if A[i - 1] == A[i]:
                while i < len(A) and A[i - 1] == A[i]:
                    i += 1
                # print 'eq end', i
            else:
                curr_mountain_start = i - 1
                while i < len(A) and A[i] > A[i - 1]:
                    i += 1
                curr_mountain_peak = i - 1
                while i < len(A) and A[i - 1] > A[i]:
                    i += 1
                curr_mountain_end = i - 1
                if curr_mountain_peak - curr_mountain_start > 0 and curr_mountain_end - curr_mountain_peak > 0:
                    longest_mountain = max(longest_mountain, curr_mountain_end - curr_mountain_start + 1)

        return longest_mountain


print Solution().longestMountain([2, 1, 4, 7, 3, 2, 5])
print Solution().longestMountain([2, 2, 2])
print Solution().longestMountain([1, 2, 1])
print Solution().longestMountain([2, 2, 2, 1])
print Solution().longestMountain([1, 2, 3, 3, 2, 1, 0])
print Solution().longestMountain([1, 2, 3, 3, 2, 1])
print Solution().longestMountain([1, 2, 3, 3, 3, 3, 3, 2, 3, 1])
print Solution().longestMountain([2, 3])
