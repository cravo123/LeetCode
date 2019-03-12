# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        self.res = max(self.res, L + node.val + R)
        
        return max(max(L, R) + node.val, 0)
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        
        return self.res