class Solution:
    # making permutations
    def permute(self, nums):
        res = []
        self.compute(0, nums, res)
        return res

    def compute(self, ind, ar, res):
        if ind == len(ar):
            res.append(ar.copy())
            return

        for i in range(ind, len(ar)):
            ar[i], ar[ind] = ar[ind], ar[i]  # swap
            self.compute(ind + 1, ar, res)
            ar[i], ar[ind] = ar[ind], ar[i]  # return to og

    # making selections and storing the choice
    #     res = []
    #     self.compute(nums, [], {}, res)
    #     return res
    #
    # def compute(self, ar, ds, m, res):
    #     if len(ds) == len(ar):
    #         res.append(ds.copy())
    #         return
    #
    #     for i in range(len(ar)):
    #
    #         if m.get(ar[i]) == 1:
    #             continue
    #
    #         ds.append(ar[i])
    #         m[ar[i]] = 1
    #         self.compute(ar, ds, m, res)
    #         m[ds.pop()] = None


sol = Solution()
print(sol.permute([1, 2, 3]))
