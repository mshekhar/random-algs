import collections


class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        # Want smallest y-x with Py - Px >= K
        ans = N + 1  # N+1 is impossible
        monoq = collections.deque()  # opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            # Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N + 1 else -1


print Solution().shortestSubarray([1, 2], 4), -1
print Solution().shortestSubarray([2, -1, 2], 3), 3
print Solution().shortestSubarray([84, -37, 32, 40, 95], 167), 3
print Solution().shortestSubarray([56, -21, 56, 35, -9], 61), 2
print Solution().shortestSubarray([1], 1), 1
print Solution().shortestSubarray([-47, 45, 92, 86, 17, -22, 77, 62, -1, 42], 180), 3
print Solution().shortestSubarray([11, 47, 97, 35, -46, 59, 46, 51, 59, 80, 14, -6, 2, 20, 96, 1, 18, 74, -17, 71],
                                  282), 5

# print Solution().shortestSubarray([1, 4, 45, 6, 10, 19], 51)
# print Solution().shortestSubarray([1, 10, 5, 2, 7], 9)
# print Solution().shortestSubarray([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280)
# print Solution().shortestSubarray([- 8, 1, 4, 2, -6], 6)
# print Solution().shortestSubarray([56, -21, 56, 35, -9], 61)
# print Solution().shortestSubarray([75, -32, 50, 32, 97], 129)
# print Solution().shortestSubarray([48, 99, 37, 4, -31], 140)

# def shortestSubarray2(self, A, K):
#     """
#     :type A: List[int]
#     :type K: int
#     :rtype: int
#     """
#     total_sum = 0
#     start = 0
#     end = 0
#     subarray_len = len(A) + 1
#     while end < len(A):
#         if end > 0:
#             end -= 1
#         start = end
#         total_sum = 0
#         while total_sum < K and end < len(A):
#             # print 't1', total_sum, A[end]
#             if A[end] >= K:
#                 return 1
#
#             total_sum += A[end]
#             # print 't1', total_sum, A[end]
#             end += 1
#             if total_sum >= K:
#                 subarray_len = end - start if end - start < subarray_len else subarray_len
#
#             if total_sum < 0:
#                 start = end
#                 total_sum = 0
#
#         if start >= len(A):
#             break
#         print 'e1', total_sum, subarray_len, end - start, end, start, A[start]
#         while total_sum - A[start] >= K and (end - start) - 1 < subarray_len:
#             print 'e2', total_sum, subarray_len, end - start, end, start, A[start]
#             total_sum -= A[start]
#             start += 1
#             subarray_len = end - start
#
#         # if total_sum >= K and end >= len(A):
#         #     sum_val = total_sum
#         #     subarray_len = end - start
#
#     # print total_sum, sum_val, subarray_len, start, end, A[start]
#     if subarray_len > len(A):
#         return -1
#     return subarray_len
