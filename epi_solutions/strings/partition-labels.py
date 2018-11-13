class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        ranges = [[float('inf'), float('-inf')] for _ in range(26)]
        for i in xrange(len(S)):
            r = ranges[ord(S[i]) - ord('a')]
            r[0] = min(i, r[0])
            r[1] = max(i, r[1])
        filtered_range = filter(lambda x: x[0] != float('inf') and x[1] != float('-inf'), ranges)
        filtered_range.sort(key=lambda x: x[0])
        res = []
        if not filtered_range:
            return []
        curr_range = filtered_range[0]
        i = 1
        while i < len(filtered_range):
            if curr_range[1] < filtered_range[i][0]:
                res.append(curr_range)
                curr_range = filtered_range[i]
            else:
                curr_range[1] = max(curr_range[1], filtered_range[i][1])
            i += 1
        if curr_range:
            res.append(curr_range)
        # print filtered_range
        # print res
        return map(lambda x: x[1] - x[0] + 1, res)


print Solution().partitionLabels("ababcbacadefegdehijhklij")
