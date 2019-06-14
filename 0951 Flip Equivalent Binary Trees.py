# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def dfs(self, p, q):
        if p is None or q is None:
            return p is q
        
        if p.val != q.val:
            return False
        
        res = self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
        res = res or (self.dfs(p.left, q.right) and self.dfs(p.right, q.left))
        
        return res
        
    def flipEquiv(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        return self.dfs(root1, root2)

# Solution 2, canonical representation
# t.b.c