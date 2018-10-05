class Solution(object):
    def get_neighbors(self, row, col, grid):
        nei = []
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if row < 0 or col < 0:
                continue
            try:
                if grid[i][j] == '1':
                    nei.append((i, j))
            except IndexError:
                continue
        return nei

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        try:
            m = len(grid)
            n = len(grid[0])
            if m < 1 or n < 1:
                return 0
        except IndexError:
            return 0

        not_visited = set()
        stack = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    not_visited.add((i, j))

        if not not_visited:
            return 0
        islands = 0
        while not_visited:
            if not stack:
                stack.append(not_visited.pop())
                islands += 1
            row, col = stack.pop()
            for i, j in self.get_neighbors(row, col, grid):
                if (i, j) in not_visited:
                    not_visited.remove((i, j))
                    stack.append((i, j))
        return islands


print Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                             ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
print Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                             ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
