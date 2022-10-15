# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allInOneTraversal(self, root):
        stack = [[root, 1]]
        # for result
        preL, inL, postL = [], [], []

        while stack:
            ele = stack.pop()
            num = ele[1]
            node = ele[0]

            print(node.val,num)
            if num == 1:  # PreOrder
                preL.append(node.val)
                stack.append([node, num + 1])  # for pre traversal num=2
                if node.left: stack.append([node.left, 1])

            if num == 2:  # InOrder
                inL.append(node.val)
                stack.append([node, num + 1])  # for pre traversal num=2
                if node.right: stack.append([node.right, 1]) # set num=1 for preOrder

            if num == 3:  # PostOrder
                postL.append(node.val)

        print("Pre: ", preL)
        print("In: ", inL)
        print("Post: ", postL)


root = TreeNode(1, None, None)

root.left = TreeNode(2, None, None)
root.left.left = TreeNode(3, None, None)
root.left.right = TreeNode(4, None, None)

root.right = TreeNode(5, None, None)
root.right.left = TreeNode(6, None, None)
root.right.right = TreeNode(7, None, None)

Solution().allInOneTraversal(root)