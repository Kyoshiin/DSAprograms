# User function Template for python3
class Solution:
    def subsetSums(self, arr, N):
        fl = []
        self.printSbS(0, arr, 0, [], fl)
        return sorted(fl)

    def printSbS(self, ind, ar, s, res, fl):
        if ind == len(ar):
            fl.append(s)
            return

        cur_ind_no = ar[ind]

        res.append(cur_ind_no)
        s += cur_ind_no
        self.printSbS(ind + 1, ar, s, res, fl)  # take
        res.pop()
        s -= cur_ind_no

        self.printSbS(ind + 1, ar, s, res, fl)  # take


sol = Solution()
print(sol.subsetSums([2, 3],2))
