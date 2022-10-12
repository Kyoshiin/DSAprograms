class Solution:
    def findPath(self, m, n):
        res = []
        vi = [(0, 0)]
        self.solve(m, n, 0, 0, [], vi, res)
        return res

    def solve(self, mat, n, row, col, ds, vi, res):
        if row == n - 1 and col == n - 1:
            res.append(''.join(ds))
            return
        if mat[row][col] == 0:  # for initial pos
            return
        # check U
        if self.checkMove(mat, n, row - 1, col, vi):
            vi.append((row - 1, col))
            ds.append('U')
            self.solve(mat, n, row - 1, col, ds, vi, res)
            vi.pop()
            ds.pop()

        # check D
        if self.checkMove(mat, n, row + 1, col, vi):
            vi.append((row + 1, col))
            ds.append('D')
            self.solve(mat, n, row + 1, col, ds, vi, res)
            vi.pop()
            ds.pop()

        # check L
        if self.checkMove(mat, n, row, col - 1, vi):
            vi.append((row, col - 1))
            ds.append('L')
            self.solve(mat, n, row, col - 1, ds, vi, res)
            vi.pop()
            ds.pop()

        # check R
        if self.checkMove(mat, n, row, col + 1, vi):
            vi.append((row, col + 1))
            ds.append('R')
            self.solve(mat, n, row, col + 1, ds, vi, res)
            vi.pop()
            ds.pop()

    def checkMove(self, mat, n, row, col, vi):
        if row == n or col == n or row < 0 or col < 0:
            return False
        if (row, col) in vi:
            return False
        if mat[row][col] == 0:
            return False

        return True


# print(Solution().findPath([[1, 0, 0, 0],
#                            [1, 1, 0, 1],
#                            [1, 1, 0, 0],
#                            [0, 1, 1, 1]], 4))

print(Solution().findPath([[1, 0],
                           [1, 0]], 2))
