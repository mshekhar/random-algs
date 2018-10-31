class Solution(object):
    def dfs(self, nums, visited, idx, seen):
        if nums[idx] in seen:
            return 0
        visited[nums[idx]] = True
        seen.add(nums[idx])
        # print 'dfs  ', nums[idx], seen, nums[nums[idx]]
        count = self.dfs(nums, visited, nums[idx], seen)
        return count + 1

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        visited = [False for _ in nums]
        max_len = 0
        for idx in xrange(len(nums)):
            if not visited[idx]:
                count = self.dfs(nums, visited, idx, set())
                max_len = max(max_len, count)
        return max_len


print Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2])
