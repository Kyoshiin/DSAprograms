# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack, res = [root], []

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res

    def inorderTraversal(self, root):  # L rt R
        stack, res = [], []
        node = root
        while True:
            if node:
                # keep on going for left subtree
                # maintain stack for all the nodes
                stack.append(node)
                node = node.left

            else:  # when there is no left/right subtree
                if not stack: break  # stack empty

                # get the visited nodes and print node (root)
                # then move root -> right
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    # using 2 stacks
    def postorderTraversal1(self, root):
        if not root: return []
        stack, resStk = [root], []

        while True:
            if not stack: break

            node = stack.pop()
            resStk.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return resStk[::-1]
