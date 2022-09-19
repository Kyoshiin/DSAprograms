class Solution:

    def combinationSum(self, candidates, target):
        res = []
        self.checkCombination(0, sorted(candidates), target, [], res)
        return res

    def checkCombination(self, ind, candidates, target, ds, res):
        if target == 0:
            res.append(ds.copy())  # only res will send a ref
            return
        if ind == len(candidates):
            return

        for i in range(ind, len(candidates)):

            if target < candidates[i]:
                break

            if i > ind and candidates[i] == candidates[i - 1]:
                continue

            ds.append(candidates[i])
            self.checkCombination(i + 1, candidates, target - candidates[i], ds, res)
            ds.pop() # cuz when recursion over, previous call ds did'nt have the cand[i]


sol = Solution()
print(sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
