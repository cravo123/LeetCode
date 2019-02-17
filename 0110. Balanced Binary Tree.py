# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion Bottom-up O(N)
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        if L < 0 or R < 0 or abs(L - R) > 1:
            return -1
        return max(L, R) + 1
        
        
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        return self.dfs(root) >= 0
