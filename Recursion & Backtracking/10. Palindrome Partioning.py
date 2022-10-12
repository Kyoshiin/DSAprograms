class Solution:
    def partition(self, s):
        res = []
        self.solve(0, s, [], res, len(s))
        return res

    def solve(self, ind, s, ds, res, n):
        if ind == n:
            res.append(ds.copy())
            print(res)
            return

        for i in range(ind, n):
            if self.checkPalin(s[ind:i + 1]):
                ds.append(s[ind:i + 1])
                print("appnd", ds, ind,i)
                self.solve(i+1, s, ds, res, n)
                print("popped",ds.pop(),ds,ind)


    def checkPalin(self, st):
        return st == st[::-1]


print("OUTPUT!!\n", Solution().partition("aabb"))
