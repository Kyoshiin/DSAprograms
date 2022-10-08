'''
Normal N-Queen Solution
'''


class Solution:
    # checking if it's safe to insert Q
    def safeToFill(self, row, col, board, n):
        trow = row
        tcol = col

        # left upr diagonal
        while trow >= 0 and tcol >= 0:
            if board[trow][tcol] == 'Q':
                return False
            trow -= 1
            tcol -= 1

        trow = row
        tcol = col

        # left of the row
        while tcol >= 0:
            if board[trow][tcol] == 'Q':
                return False
            tcol -= 1

        trow = row
        tcol = col

        # left lwr diagonal
        while trow < n and tcol >= 0:
            if board[trow][tcol] == 'Q':
                return False
            trow += 1
            tcol -= 1

        return True

    def solve(self, col, n, board, res):
        if col == n:
            tboard = []
            for row in board:  # cuz py uses ref
                tboard.append("".join(row))
            res.append(tboard.copy())
            return

        for row in range(n):
            if self.safeToFill(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col + 1, n, board, res)
                board[row][col] = '.'  # backtracking

    def solveNQueens(self, n: int):
        res = []
        board = [['.'] * n for _ in range(n)]

        self.solve(0, n, board, res)

        return res


print("OUTPUT!!\n", Solution().solveNQueens(4))
