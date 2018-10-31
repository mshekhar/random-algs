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

    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        max_till_now = self.get_max_till_now(A)
        min_after_now = self.get_min_after_now(A)
        for i in xrange(len(A)):
            if max_till_now[i] <= min_after_now[i]:
                return i + 1
        return i + 1

        # print A
        # print max_till_now
        # print min_after_now


print Solution().partitionDisjoint([1, 1, 1, 0, 6, 12])
print Solution().partitionDisjoint([5, 0, 3, 8, 6])
print Solution().partitionDisjoint([8, 6, 5, 0, 3, 8, 6])
print Solution().partitionDisjoint([8, 6, 5, 3, 0])
print Solution().partitionDisjoint([0, 6, 5, 3, 1])
