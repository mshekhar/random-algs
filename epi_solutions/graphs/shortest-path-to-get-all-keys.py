from Queue import Queue


class State(object):
    def __init__(self, x, y, keys, path_len):
        self.x = x
        self.y = y
        self.keys = keys
        self.path_len = path_len

    def __key(self):
        return (self.x, self.y, tuple(self.keys))

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        try:
            m = len(grid)
            n = len(grid[0])
            if m < 1 or n < 1:
                return -1
        except IndexError:
            return -1
        start_i = -1
        start_j = -1
        key_count = 0
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '@':
                    start_i = i
                    start_j = j
                elif ord('a') <= ord(grid[i][j]) <= ord('f'):
                    key_count += 1

        q = Queue()
        visited = set()
        start_state = State(x=start_i, y=start_j, keys=['0'] * key_count, path_len=0)
        q.put(start_state)
        visited.add(start_state)
        # print start_i, start_j, key_count
        while q.qsize() > 0:
            state = q.get()
            for nei in neighbors:
                if not (0 <= (state.x + nei[0]) < m and 0 <= (state.y + nei[1]) < n):
                    continue
                new_state = State(x=state.x + nei[0], y=state.y + nei[1], keys=state.keys[:],
                                  path_len=state.path_len + 1)
                # print new_state.x, new_state.y, state.x, state.y, nei, state.x + nei[0], m, state.y + nei[1], n
                if ord('a') <= ord(grid[new_state.x][new_state.y]) <= ord('f'):
                    new_state.keys[ord(grid[new_state.x][new_state.y]) - ord('a')] = '1'

                if new_state.keys.count('1') == key_count:
                    return new_state.path_len

                if grid[new_state.x][new_state.y] == '#':
                    continue

                is_lock = ord('A') <= ord(grid[new_state.x][new_state.y])
                if is_lock:
                    key_acquired = new_state.keys[ord(grid[new_state.x][new_state.y].lower()) - ord('a')] == '1'
                    if not key_acquired:
                        continue

                if new_state not in visited:
                    # print new_state.path_len, grid[new_state.x][new_state.y], new_state.keys, new_state.x, new_state.y, state.x, state.y
                    visited.add(new_state)
                    q.put(new_state)
        return -1


try:
    print Solution().shortestPathAllKeys(["@..aA", "..B#.", "....b"])
    print Solution().shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"])
    print Solution().shortestPathAllKeys(["@...a", ".###A", "b.BCc"])
except:
    import time

    time.sleep(0.2)
    raise
