# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0 # increasing, decreasing
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        L_i = L[0] if node.left and node.left.val + 1 == node.val else 0
        L_d = L[1] if node.left and node.left.val - 1 == node.val else 0
        
        R_i = R[0] if node.right and node.right.val + 1 == node.val else 0
        R_d = R[1] if node.right and node.right.val - 1 == node.val else 0
        
        self.res = max(self.res, L_i + 1 + R_d, L_d + 1 + R_i)
        
        i = max(L_i, R_i) + 1
        d = max(L_d, R_d) + 1
        return i, d
        
        
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root)
        
        return self.res