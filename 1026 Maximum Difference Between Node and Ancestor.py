# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, low, up):
        if node is None:
            return 0
        res = max(abs(node.val - low), abs(node.val - up))
        
        low = min(low, node.val)
        up = max(up, node.val)
        
        res = max(res, self.dfs(node.left, low, up))
        res = max(res, self.dfs(node.right, low, up))
        
        return res
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = self.dfs(root, root.val, root.val)
        
        return res