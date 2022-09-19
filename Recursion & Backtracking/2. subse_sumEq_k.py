'''1. Printing all subsequences whose sum is k'''
def printSbS(ind, ar, k, sum, res):
    if ind == len(ar):
        if sum == k:
            print(res)
        return

    cur_ind_no = ar[ind]

    res.append(cur_ind_no)
    sum += cur_ind_no
    printSbS(ind + 1, ar, k, sum, res)  # take

    res.pop()
    sum -= cur_ind_no

    printSbS(ind + 1, ar, k, sum, res)  # not take


'''2. Printing only 1 subsequence whose sum is k'''
def printOneSb(ind, ar, k, sum, res):
    # condition satisfied
    if ind == len(ar):
        if sum == k:
            print(res)
            return True

        return False  # when condition not satisfied

    cur_ind_no = ar[ind]

    res.append(cur_ind_no)
    sum += cur_ind_no
    if printOneSb(ind + 1, ar, k, sum, res) == True:  # take
        return True

    res.pop()
    sum -= cur_ind_no

    if printOneSb(ind + 1, ar, k, sum, res) == True:  # not take
        return True

    return False  # when no subsq exit


'''3. Printing count of subsequences whose sum is k'''
def printSbCount(ind, ar, k, sum):
    # condition satisfied
    if ind == len(ar):
        if sum == k:
            # print(res)
            return 1
        return 0  # when condition not satisfied

    cur_ind_no = ar[ind]

    sum += cur_ind_no
    l = printSbCount(ind + 1, ar, k, sum)  # take / left recursion / count of subsq

    sum -= cur_ind_no

    r = printSbCount(ind + 1, ar, k, sum)  # not take / right recursion / count of subsq

    return l + r


# calling method
# printSbS(0, [1, 2, 1], 2, 0, [])
printOneSb(0, [2,2,3],7, 0, [])
# print(printSbCount(0, [2,2,3],7, 0))
