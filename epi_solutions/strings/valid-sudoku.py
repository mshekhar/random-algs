class Solution(object):
    def are_rows_valid(self, board):
        for row in xrange(9):
            numbers_set = set()
            for col in xrange(9):
                if not ord('0') <= ord(board[row][col]) <= ord('9'):
                    continue
                if board[row][col] in numbers_set:
                    return False
                numbers_set.add(board[row][col])
        return True

    def are_cols_valid(self, board):
        for col in xrange(9):
            numbers_set = set()
            for row in xrange(9):
                if not ord('0') <= ord(board[row][col]) <= ord('9'):
                    continue
                if board[row][col] in numbers_set:
                    return False
                numbers_set.add(board[row][col])
        return True

    def are_boxes_valid(self, board):
        for row_st in [0, 3, 6]:
            for col_st in [0, 3, 6]:
                numbers_set = set()
                for row in range(3):
                    for col in range(3):
                        if not ord('0') <= ord(board[row_st + row][col_st + col]) <= ord('9'):
                            continue
                        if board[row_st + row][col_st + col] in numbers_set:
                            return False
                        numbers_set.add(board[row_st + row][col_st + col])
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.are_boxes_valid(board) and self.are_cols_valid(board) and self.are_rows_valid(board)


print Solution().isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
print Solution().isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
