import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, BFS level traversal
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res_level = None
        res_val = float('-inf')
        
        q = [root]
        level = 1
        while q:
            curr_val = sum(p.val for p in q)
            if curr_val > res_val:
                res_level, res_val = level, curr_val
            
            q = [x for p in q for x in [p.left, p.right] if x]
            level += 1
        
        return res_level

# Solution 2, DFS recursion
class Solution:
    def dfs(self, node, level, d):
        if node is None:
            return
        d[level] += node.val
        level += 1
        self.dfs(node.left, level, d)
        self.dfs(node.right, level, d)
        
    def maxLevelSum(self, root: TreeNode) -> int:
        d = collections.Counter()
        
        self.dfs(root, 1, d)
        
        res_val = max(d.values())
        
        for level in sorted(d):
            if d[level] == res_val:
                return level