# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root):
        # (node,verti,level)
        queue = [(root, 0, 0)]
        ds = defaultdict(lambda: defaultdict(list))
        res=[]

        while queue:
            cur_tup = queue.pop(0)
            cur_node = cur_tup[0]
            cur_verti = cur_tup[1]
            cur_level = cur_tup[2]

            # adding to ds
            # vertical -> level -> node
            ds[cur_verti][cur_level].append(cur_node.val)

            # if child nodes exists add them
            # left child v-1, l+1
            # right child v+1, l+1
            if cur_node.left:
                queue.append((cur_node.left, cur_verti - 1, cur_level + 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_verti + 1, cur_level + 1))
        # print(ds)

        # getting the verticals in asc order
        for verti in sorted(ds.keys()):
            verti_list = [] # for each vertical, list of elements

            # getting all elements of all levels of cur vertical
            for level in ds[verti]:
                verti_list.extend(sorted(ds[verti][level])) # adding elements elements of vertical verti and level level
            res.append(verti_list)
        return res
