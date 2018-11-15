class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        prefix_sum = 0
        prefix_sum_list = [0] * (len(A) + 1)
        prefix_sum_list[0] += 1
        for i in A:
            prefix_sum += i
            if prefix_sum - S >= 0:
                res += prefix_sum_list[prefix_sum - S]
            prefix_sum_list[prefix_sum] += 1
            # print prefix_sum_list
        return res


print Solution().numSubarraysWithSum(A=[0, 0, 1, 1, 0, 0, 1, 0, 1], S=2)
print Solution().numSubarraysWithSum(A=[1, 0, 1, 0, 1], S=2)
print Solution().numSubarraysWithSum([1, 1, 1, 1, 1], 5)
