# Python pass by value or reference
# https://web.archive.org/web/20120615042202/http://testingreflections.com/node/view/5126

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# max height of left+right Tree
class Solution:
    maxi = 0  # or pass by list as it is mutable while integers are not

    def diameterOfBinaryTree(self, root):
        self.findmax(root)
        return self.maxi

    def findmax(self, node):
        if not node: return 0

        lh = self.findmax(node.left)
        rh = self.findmax(node.right)
        # storing max sum of height of left & right subtree
        self.maxi = max(self.maxi, lh + rh)
        return 1 + max(lh, rh)  # returning height from a node