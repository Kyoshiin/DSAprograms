'''
All other recursive DFS traversal will be same
change the func call arrangements
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def preorderTraversal(self, root):
        path = []
        self.traverse(root, path)
        return path

    def traverse(self, root, path):
        if root == None:
            return

        path.append(root.val)
        self.traverse(root.left, path)
        self.traverse(root.right, path)

