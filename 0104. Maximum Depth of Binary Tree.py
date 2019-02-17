# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        return 1 + max(self.dfs(node.left), self.dfs(node.right))
        
        
    def maxDepth(self, root: 'TreeNode') -> 'int':
        return self.dfs(root)

# Iteration
class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        level = 0
        
        if root is None:
            return level
        
        q = [root]
        
        while q:
            level += 1
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return level
