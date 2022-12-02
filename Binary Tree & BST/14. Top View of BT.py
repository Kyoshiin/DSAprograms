# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        queue = [(root, 0)]
        ds = {}
        res = []

        while queue:
            cur_ele = queue.pop(0)
            cur_node = cur_ele[0]
            cur_v = cur_ele[1]

            # check if vertical already there
            # adding to ds
            if cur_v not in ds.keys():
                ds[cur_v] = cur_node.data

            if cur_node.left:
                queue.append((cur_node.left, cur_v - 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_v + 1))

        for ver in sorted(ds.keys()):
            res.append(ds[ver])

        return res
