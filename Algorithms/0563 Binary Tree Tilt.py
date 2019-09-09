# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        return L[0] + R[0] + node.val, L[1] + R[1] + abs(L[0] - R[0])
    
    def findTilt(self, root: TreeNode) -> int:
        _, res = self.dfs(root)
        
        return res