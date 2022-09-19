class Solution:

    def combinationSum(self, candidates, target):
        fl = []
        self.checkCombination(0, candidates, target, [], fl)
        return fl

    def checkCombination(self, i, cl, k, res, fl):
        if k == 0:
            fl.append(res.copy()) # only res will send a ref
            return
        # if ind == len(candidates) or k < candidates[ind]: # works only if it's a sorted list
        #     return
        if i == len(cl):
            return

        if k >= cl[i]:
            res.append(cl[i])
            # not incrementing ind as repetition allowed
            self.checkCombination(i, cl, k - cl[i], res, fl)  # taking the ele at ind
            res.pop()

        # incrementing ind but not choosing ele[ind]
        self.checkCombination(i + 1, cl, k, res, fl)  # taking the ele at ind


sol = Solution()
print(sol.combinationSum([8, 7, 4, 3], 11))
