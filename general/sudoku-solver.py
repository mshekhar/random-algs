class Solution(object):
    def is_row_valid(self, row, board, num):
        for col in board[row]:
            if col == num:
                return False
        return True

    def is_col_valid(self, col, board, num):
        for row in board:
            if row[col] == num:
                return False
        return True

    def is_box_valid(self, row_st, col_st, board, num):
        for row in range(3):
            for col in range(3):
                if board[row_st + row][col_st + col] == num:
                    return False
        return True

    def is_valid(self, row, col, board, num):
        if self.is_row_valid(row, board, num) and \
                self.is_col_valid(col, board, num) and \
                self.is_box_valid(row - (row % 3), col - (col % 3), board, num):
            return True
        return False

    def helper(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_size = 9
        for row in range(board_size):
            for col in range(board_size):
                # print board[row][col] == '.', board[row][col]
                if board[row][col] == '.':
                    for num in range(1, board_size + 1):
                        # print 'is_valid ', self.is_valid(row, col, board, str(num))
                        if self.is_valid(row, col, board, str(num)):
                            board[row][col] = str(num)
                            if self.helper(board):
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return True

    def solveSudoku(self, board):
        self.helper(board)

    def print_and_solve(self, arr, expected):
        for i in arr:
            print i
        print 'solve ', self.solveSudoku(arr)
        for c, i in enumerate(arr):
            if expected:
                print i, expected[c], i == expected[c]
            else:
                print i
        print '\n'


b1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
expected_b1 = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
               ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
               ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
               ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
               ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
               ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
               ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
               ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
               ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
Solution().print_and_solve(b1, expected_b1)
b2 = [['.', '9', '.', '.', '.', '.', '8', '5', '3'],
      ['.', '.', '.', '8', '.', '.', '.', '.', '4'],
      ['.', '.', '8', '2', '.', '3', '.', '6', '9'],
      ['5', '7', '4', '.', '.', '2', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '9', '.', '.', '6', '3', '7'],
      ['9', '4', '.', '1', '.', '8', '5', '.', '.'],
      ['7', '.', '.', '.', '.', '6', '.', '.', '.'],
      ['6', '8', '2', '.', '.', '.', '.', '9', '.']]
Solution().print_and_solve(b2, None)
