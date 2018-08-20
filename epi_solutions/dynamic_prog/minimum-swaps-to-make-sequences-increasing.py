class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        swapped = [1.0]
        not_swapped = [0.0]
        for i in range(1, len(A)):
            # prev swapped
            s1, ns1 = float('inf'), float('inf')
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                ns1 = swapped[i - 1]
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                s1 = swapped[i - 1] + 1

            # prev not swapped
            s2, ns2 = float('inf'), float('inf')
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                ns2 = not_swapped[i - 1]
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                s2 = not_swapped[i - 1] + 1

            not_swapped.append(min(ns1, ns2))
            swapped.append(min(s1, s2))

        # print A
        # print B
        # print swapped
        # print not_swapped
        return int(min(swapped[-1], not_swapped[-1]))


Solution().minSwap([1, 3, 5, 4, 9], [1, 2, 3, 7, 10])
Solution().minSwap([10, 15, 29, 30, 31], [9, 21, 20, 28, 40])
