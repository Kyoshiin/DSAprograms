# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        queue = [(root, 0)]  # (node,level)
        ds = {}
        res = []

        if not root:
            return res

        while queue:
            cur_ele = queue.pop(0)
            cur_node = cur_ele[0]
            cur_level = cur_ele[1]

            # adding to ds
            ds[cur_level] = cur_node.val

            if cur_node.left:
                queue.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_level + 1))

        for l in sorted(ds.keys()):
            res.append(ds[l])

        return res