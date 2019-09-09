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
        
        return node.val + L[1] + R[1], max(L) + max(R)
        
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))