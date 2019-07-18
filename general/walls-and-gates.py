from Queue import Queue


class Solution(object):
    INF = 2147483647

    def get_neighbors(self, row, col, rooms):
        nei = []
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if i < 0 or j < 0:
                continue
            try:
                if rooms[i][j] == Solution.INF:
                    nei.append((i, j))
            except IndexError:
                continue
        return nei

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        q = Queue()
        try:
            m = len(rooms)
            n = len(rooms[0])
            if m < 1 or n < 1:
                return
        except IndexError:
            return

        arr = []
        for (i, j) in filter(lambda (x, y): rooms[x][y] == 0, ((i, j) for j in xrange(n) for i in xrange(m))):
            # print i, j
            # if (i == 3 and j == 2) or (i == 3 and j == 3):
            #     import pdb
            #     pdb.set_trace()
            q.put((i, j))
            arr.append((i, j))

        # print arr

        while q.qsize() > 0:
            row, col = q.get()
            for new_row, new_col in self.get_neighbors(row, col, rooms):
                # print new_row, new_col
                # if (new_row == 3 and new_col == 2) or (new_row == 3 and new_col == 3):
                #     import pdb
                #     pdb.set_trace()
                rooms[new_row][new_col] = rooms[row][col] + 1
                q.put((new_row, new_col))

    @classmethod
    def runner(cls, rooms):
        print '\n'
        for r in rooms:
            print r

        print '\n'
        Solution().wallsAndGates(rooms)

        for r in rooms:
            print r


Solution.runner([[2147483647, -1, 0, 2147483647],
                 [2147483647, 2147483647, 2147483647, -1],
                 [2147483647, -1, 2147483647, -1],
                 [0, -1, 2147483647, 2147483647]])
Solution.runner([[]])
Solution.runner([[-1]])
Solution.runner([[2147483647]])
Solution.runner([[0]])
Solution.runner([[2147483647, 0, 2147483647, 2147483647, 0, 2147483647, -1, 2147483647]])


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = {i[0] + str(len(i) - 2) + i[-1] if len(i) > 2 else i for i in dictionary}

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return not (word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word in self.d)

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
