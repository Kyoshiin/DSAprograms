# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        res = []
        if root is None:  # root is null
            return res
        queue = [root]

        while queue:
            size = len(queue)
            levelList = []

            for _ in range(size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)  # if present
                if node.right: queue.append(node.right)
                levelList.append(node.val)

            res.append(levelList)
        return res
