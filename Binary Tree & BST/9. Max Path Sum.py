# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float("-inf")  # for accepting nodes.val = -ve no

    def maxPathSum(self, root):
        self.maxPath(root)
        return self.maxi

    # finding the max path then calc sum
    def maxPath(self, node):
        if not node: return 0

        # only take positive sums
        leftSum = max(0, self.maxPath(node.left))
        rightSum = max(0, self.maxPath(node.right))
        # storing max of an umbrella path
        self.maxi = max(self.maxi, leftSum + rightSum + node.val)
        return node.val + max(leftSum, rightSum)
