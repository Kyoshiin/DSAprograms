class Solution:
    def getPermutation(self, n: int, k: int):
        fact = 1
        ar = []
        k -= 1  # 0 based indexing
        for i in range(1, n):
            fact *= i  # n-1 ! needed
            ar.append(i)

        ar.append(n)
        res = ""  # resultant string
        while True:
            res += str(ar[k // fact])  # chosing no for k
            ar.remove(ar[k // fact])

            if len(ar) == 0:
                break

            k = k % fact
            # cuz fact is changed to (n-i)!
            fact = fact // len(ar)

        return res


print(Solution().getPermutation(3, 5))
