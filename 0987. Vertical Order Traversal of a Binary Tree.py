# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def dfs(self, node, x, y, d):
        if node is None:
            return
        if y not in d[x]:
            d[x][y] = []
        d[x][y].append(node.val)
        self.dfs(node.left, x - 1, y + 1, d)
        self.dfs(node.right, x + 1, y + 1, d)
        
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        d = collections.defaultdict(dict)
        
        self.dfs(root, 0, 0, d)
        
        res = []
        
        for x in sorted(d):
            tmp = []
            for y in sorted(d[x]):
                tmp.extend(list(sorted(d[x][y])))
            res.append(tmp)
        
        return res