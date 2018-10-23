class Solution(object):
    def helper(self, row, col, board, word, word_idx, m, n):
        if word_idx == len(word):
            return True
        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        if board[row][col] == word[word_idx]:
            board[row][col] = '!'
            res = self.helper(row + 1, col, board, word, word_idx + 1, m, n) or \
                  self.helper(row - 1, col, board, word, word_idx + 1, m, n) or \
                  self.helper(row, col + 1, board, word, word_idx + 1, m, n) or \
                  self.helper(row, col - 1, board, word, word_idx + 1, m, n)
            board[row][col] = word[word_idx]
            # print 'is_valid ', self.is_valid(row, col, board, str(num))
            return res
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        try:
            m = len(board)
            n = len(board[0])
            if m < 1 or n < 1:
                return False
        except IndexError:
            return False
        for row in xrange(m):
            for col in xrange(n):
                if self.helper(row, col, board, word, 0, m, n):
                    return True
        return False


print Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCCED")
print Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "SEE")
print Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCB")

print Solution().exist([["a"]], "a")
