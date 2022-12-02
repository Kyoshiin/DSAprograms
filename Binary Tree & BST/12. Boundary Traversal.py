'''
Q Link: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Node:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None
'''


class Solution:
    def getLeftBoundary(self, root, ds):
        cur_node = root.left
        while cur_node:
            if not self.isLeaf(cur_node):  # not a leaf
                ds.append(cur_node.data)
            if cur_node.left:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

    def getRightBoundary(self, root, ds):
        rbNodes = []
        cur_node = root.right
        while cur_node:
            if not self.isLeaf(cur_node):
                rbNodes.append(cur_node.data)
            if cur_node.right:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        # reverse and add
        ds.extend(rbNodes[::-1])

    def printBoundaryView(self, root):
        ds = []
        if not root:
            return ds
        if not self.isLeaf(root):
            ds = [root.data]

        # getting left boundary nodes
        self.getLeftBoundary(root, ds)
        # getting leaf nodes
        self.getLeaves(root, ds)
        # getting right boundary nodes in reverse
        self.getRightBoundary(root, ds)

        return ds

    def getLeaves(self, root, leafNodes):
        if not root:
            return

        if self.isLeaf(root):
            leafNodes.append(root.data)
        self.getLeaves(root.left, leafNodes)
        self.getLeaves(root.right, leafNodes)

    def isLeaf(self, node):
        return node.left is None and node.right is None
