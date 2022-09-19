# program to print subsequences recursively

def printS(ind, nl, n, res):
    if ind >= n:
        # print(' '.join([str(ind) for ind in res]))
        print(res)
        return

    res.append(nl[ind])
    printS(ind + 1, nl, n, res)  # take

    res.pop()
    printS(ind + 1, nl, n, res)  # not take


printS(0, [3, 1, 2], 3, [])
