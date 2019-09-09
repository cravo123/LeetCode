# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
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

# Solution 1.1, recursion with global variable
class Solution:
    def dfs(self, node, lo, hi):
        if node is None:
            return
        self.res = max(self.res, abs(lo - node.val), abs(hi - node.val))
        lo = min(lo, node.val)
        hi = max(hi, node.val)
        
        self.dfs(node.left, lo, hi)
        self.dfs(node.right, lo, hi)
        
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root, root.val, root.val)
        
        return self.res