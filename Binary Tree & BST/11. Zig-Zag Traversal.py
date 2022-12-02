# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        # level order traversal
        # rev for printing,1 st, -1 rev
        res = []
        isReverse = 1
        queue = [root]

        if root is None:  # root is null
            return res

        while queue:  # while q not empty
            levelList = []
            size = len(queue)

            for _ in range(size):
                # take first q ele
                node = queue.pop(0)
                # check child nodes
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                # add cur node to level list
                levelList.append(node.val)
            # add to res and change rev
            res.append(levelList[::isReverse])
            isReverse *= -1
        return  res
