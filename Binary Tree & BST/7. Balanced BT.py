# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # naive approach
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1: return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):  # if any node is not balanced
            return False
        return True

    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    # Optimised
    def isBalanced2(self, root):
        if not root:
            return True
        return self.height2(root) >= 0

    # not calc full height if diff >1
    def height2(self, root):
        if not root: return 0
        lh = self.height2(root.left)
        rh = self.height2(root.right)

        if lh == -1 or rh == -1: return -1
        if abs(lh - rh) > 1: return -1
        return 1 + max(lh, rh)
