class CountClass(object):
    def __init__(self):
        self.x = 0

    def incr(self):
        self.x += 1

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return str(self.x)

    def __cmp__(self, other):
        if isinstance(other, CountClass):
            return cmp(self.x, other.x)
        return cmp(self.x, other)


class Solution(object):
    def get_neighbors(self, row, col, grid):
        nei = []
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if row < 0 or col < 0:
                continue
            try:
                if grid[i][j] == 1:
                    nei.append((i, j))
            except IndexError:
                continue
        return nei

    def find_islands(self, grid):
        try:
            m = len(grid)
            n = len(grid[0])
            if m < 1 or n < 1:
                return {}
        except IndexError:
            return {}

        not_visited = set()
        visited = {}
        stack = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    not_visited.add((i, j))

        if not not_visited:
            return {}
        islands = 0
        while not_visited:
            if not stack:
                counter = CountClass()
                counter.incr()
                start_row, start_col = not_visited.pop()
                stack.append((start_row, start_col))
                visited[(start_row, start_col)] = counter
                islands += 1
            row, col = stack.pop()
            for i, j in self.get_neighbors(row, col, grid):
                if (i, j) in not_visited:
                    counter.incr()
                    visited[(i, j)] = counter
                    not_visited.remove((i, j))
                    stack.append((i, j))
        return visited

    def get_zero_neighbors(self, row, col, grid):
        nei = []
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if row < 0 or col < 0:
                continue
            try:
                if not grid[i][j]:
                    nei.append((i, j))
            except IndexError:
                continue
        return nei

    def count_non_zero_neighbors(self, row, col, visited):
        uniq = set()
        count = 0
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if row < 0 or col < 0:
                continue
            try:
                if visited.get((i, j)) and id(visited.get((i, j))) not in uniq:
                    count += visited.get((i, j)).x
                    uniq.add(id(visited.get((i, j))))
            except IndexError:
                continue
        return count

    def count_zero_island_size(self, grid):
        try:
            m = len(grid)
            n = len(grid[0])
            if m < 1 or n < 1:
                return 0
        except IndexError:
            return 0
        visited = self.find_islands(grid)
        if not visited:
            return 1
        # print visited
        zeros = set()
        for i, j in visited:
            for zi, zj in self.get_zero_neighbors(i, j, grid):
                zeros.add((zi, zj))

        max_nei = max(visited.itervalues())
        for zi, zj in zeros:
            max_nei = max(max_nei, self.count_non_zero_neighbors(zi, zj, visited) + 1)
        return max_nei

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = self.count_zero_island_size(grid)
        try:
            return res.x
        except AttributeError:
            return res
        # return max_nei, max(visited.values()), visited.values()


print Solution().largestIsland([[1, 1, 1, 1, 0],
                                [1, 1, 0, 1, 0],
                                [1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0]])
print Solution().largestIsland([[1, 1, 0, 0, 0],
                                [1, 1, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 1, 1]])
print Solution().largestIsland([[1, 0], [0, 1]])
print Solution().largestIsland([[1, 1], [1, 0]])
print Solution().largestIsland([[1, 1], [1, 1]])
print Solution().largestIsland([[0, 0], [0, 0]])
print Solution().largestIsland([[0, 0]])
print Solution().largestIsland([[]])
print Solution().largestIsland([[1]])
