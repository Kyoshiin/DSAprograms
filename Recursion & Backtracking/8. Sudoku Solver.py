class Solution:
    def solveSudoku(self, board):
        board = board  # reference attr for the class
        self.solve(board)

    def solve(self, board):

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':  # checking for empty place
                    for c in range(1, 10):
                        c = str(c)
                        if self.isValid(board, i, j, c):
                            board[i][j] = c

                            if self.solve(board) == True:
                                return True
                            else:
                                board[i][j] = '.'
                    return False  # when nothing can be placed

        return True  # when board is filled

    def isValid(self, board, row, col, c):
        for k in range(9):
            if board[k][col] == c:  # checking col
                return False
            if board[row][k] == c:  # checking row
                return False
            # checking  each 3X3 matrix
            if board[3 * (row // 3) + k // 3][3 * (col // 3) + k % 3] == c:
                return False
        return True
