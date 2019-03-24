# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, None
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        L_c = L[0] if L[1] == node.val else 0
        R_c = R[0] if R[1] == node.val else 0
        curr = L_c
        curr += R_c
        
        self.res = max(self.res, curr)
        
        return max(L_c, R_c) + 1, node.val
        
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root)
        
        return self.res