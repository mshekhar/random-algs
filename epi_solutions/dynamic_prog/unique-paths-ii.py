class Solution(object):
    def __init__(self):
        self.res = 0
        self.obstacleGrid = []
        self.started = set()
        self.dp = {}
        self.used_counter = {}

    def val_hash_func(self, x):
        return x

    def is_idx_valid(self, k1, k2):
        if k1 < 0 or k2 < 0:
            return False
        try:
            _ = self.obstacleGrid[k1][k2]
        except IndexError:
            return False
        return True and not self.obstacleGrid[k1][k2]

    def get_valid_neighbors(self, i, j):
        for k1, k2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            hash_key = self.val_hash_func((k1, k2))
            if self.is_idx_valid(k1, k2) and self.dp.get(hash_key, None) != -1:
                yield k1, k2

    def helper(self, c1, c2, m, n):
        if not self.is_idx_valid(c1, c2):
            return 0
        if c1 == m - 1 and c2 == n - 1:
            return 1
        hash_key = self.val_hash_func((c1, c2))
        if hash_key not in self.used_counter:
            self.used_counter[hash_key] = 0
        if hash_key not in self.dp:
            paths = 0
            self.dp[hash_key] = -1
            for k1, k2 in self.get_valid_neighbors(c1, c2):
                if k1 == m - 1 and k2 == n - 1:
                    paths += 1
                    continue
                paths += self.helper(k1, k2, m, n)
            self.dp[hash_key] = paths
        self.used_counter[hash_key] += self.dp[hash_key]
        return self.dp[hash_key]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        self.obstacleGrid = obstacleGrid
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        res = self.helper(0, 0, m, n)
        return res


s = Solution()
print s.uniquePathsWithObstacles([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
])
print s.used_counter
print s.dp
