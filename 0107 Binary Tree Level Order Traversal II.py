# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, level, res):
        if node is None:
            return
        
        if level >= len(res):
            res.append([])
        
        self.dfs(node.left, level + 1, res)
        res[level].append(node.val)
        self.dfs(node.right, level + 1, res)
        
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        
        self.dfs(root, 0, res)
        
        return res[::-1]

# Iteration
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        
        if root is None:
            return res
        
        q = [root]
        
        while q:
            res.append([p.val for p in q])
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return res[::-1]
