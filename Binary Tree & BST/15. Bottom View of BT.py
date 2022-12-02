# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
class Solution:
    def bottomView(self, root):
        queue = [(root, 0)]  # (node,vertical)
        ds = {}
        res = []

        # doing level order traversal
        while queue:
            cur_ele = queue.pop(0)
            cur_node = cur_ele[0]
            cur_vertical = cur_ele[1]

            # adding to ds
            ds[cur_vertical] = cur_node

            # checking for child nodes
            if cur_node.left: queue.append((cur_node.left, cur_vertical - 1))
            if cur_node.right: queue.append((cur_node.right, cur_vertical + 1))

        for ver in sorted(ds.keys()):
            res.append(ds[ver])

        return res
