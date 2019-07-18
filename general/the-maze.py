from Queue import Queue


class Solution(object):
    def get_neighbors(self, maze, m, n, x, y):
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if i < 0 or j < 0 or i >= m or j >= n:
                yield i, j, 1
            else:
                yield i, j, maze[i][j]

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        try:
            m = len(maze)
            n = len(maze[0])
            if m < 1 or n < 1:
                return -1
        except IndexError:
            return -1
        visited = [[0 for _ in range(n)] for _ in range(m)]
        count_0 = 0
        for dest_x, dest_y, val in self.get_neighbors(maze, m, n, destination[0], destination[1]):
            if val == 0:
                count_0 += 1
        if count_0 > 1:
            # print 'count 0 more than 1'
            return False
        q = Queue()
        q.put(start)
        while q.qsize() > 0:
            i, j = q.get()
            visited[i][j] = 1
            for x, y, val in self.get_neighbors(maze, m, n, i, j):
                # print x, y, val, destination
                if [x, y] == destination:
                    return True
                if val == 0 and visited[x][y] == 0:
                    q.put((x, y))
        return False


print Solution().hasPath([[0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 0, 0, 0, 0]],
                         [0, 4], [4, 4])
print Solution().hasPath([[0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 0, 0, 0, 0]],
                         [0, 4], [3, 2])
print Solution().hasPath([[0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 0, 0, 0, 0]],
                         [0, 4], [1, 2])
