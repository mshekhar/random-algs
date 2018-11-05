class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        buckets = [0] * (len(citations) + 1)

        for i in citations:
            bucket_idx = -1 if i > len(citations) else i
            buckets[bucket_idx] += 1
            # print i, bucket_idx, buckets

        # print buckets

        num_greater_eq = 0
        for i in xrange(len(buckets) - 1, -1, -1):
            num_greater_eq += buckets[i]
            if num_greater_eq >= i:
                return i
        return 0


print Solution().hIndex([3, 0, 6, 1, 5])
print Solution().hIndex([1])
print Solution().hIndex([0])
print Solution().hIndex([2])
print Solution().hIndex([])
