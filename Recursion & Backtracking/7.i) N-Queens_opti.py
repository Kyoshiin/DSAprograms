'''
Optimised N-Queen Solution
'''


class Solution:

    def solve(self, col, n, board, res, leftrow, leftLowDia, leftUprDia):
        if col == n:
            tboard = []
            for row in board:  # cuz py uses ref
                tboard.append("".join(row))
            res.append(tboard.copy())
            return

        for row in range(n):
            if leftrow[row] == 0 and leftLowDia[row + col] == 0 and leftUprDia[(n - 1) + (col - row)] == 0:
                board[row][col] = 'Q'
                leftrow[row] = 1
                leftLowDia[row + col] = 1
                leftUprDia[(n - 1) + (col - row)] = 1
                self.solve(col + 1, n, board, res, leftrow, leftLowDia, leftUprDia)
                # backtracking
                board[row][col] = '.'
                leftrow[row] = 0
                leftLowDia[row + col] = 0
                leftUprDia[(n - 1) + (col - row)] = 0

    def solveNQueens(self, n: int):
        res = []
        board = [['.'] * n for _ in range(n)]

        leftrow = [0] * n
        leftLowDia = [0] * (2*n-1)
        leftUprDia = [0] * (2*n-1)

        self.solve(0, n, board, res, leftrow, leftLowDia, leftUprDia)

        return res


print("OUTPUT!!\n", Solution().solveNQueens(4))
