from Queue import Queue


class Solution(object):
    end_point = '123450'

    def __init__(self):
        self.visited = {}
        self.queue = Queue()

    def swap_zero(self, cur_pos, idx, idx_0):
        if idx_0 == 2 and idx == 3:
            return None
        if idx_0 == 3 and idx == 2:
            return None
        if 5 >= idx >= 0:
            pos_lst = list(cur_pos)
            pos_lst[idx_0], pos_lst[idx] = pos_lst[idx], pos_lst[idx_0]
            return "".join(pos_lst)
        return None

    def get_next_valid_states(self, cur_pos):
        idx_0 = cur_pos.index('0')
        possible_states = [idx_0 - 1, idx_0 + 1, idx_0 - 3, idx_0 + 3]
        for state in possible_states:
            new_str = self.swap_zero(cur_pos, state, idx_0)
            if new_str and new_str not in self.visited:
                yield new_str

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board = board[0] + board[1]
        start_point = "".join(str(x) for x in board)
        if start_point == self.end_point:
            return 0
        self.queue.put((start_point, 0, [start_point]))
        while self.queue.qsize() > 0:
            cur_pos, counter, path = self.queue.get()
            self.visited[cur_pos] = True
            # print cur_pos, counter, path
            for new_str in self.get_next_valid_states(cur_pos):
                if new_str == self.end_point:
                    # print 'path ', path, new_str
                    return counter + 1
                self.queue.put((new_str, counter + 1, path + [new_str]))
        return -1


print Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]])
print Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]])
print Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])
print Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]])
