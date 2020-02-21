# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, DFS
class Solution:
    def total(self, node):
        if node is None:
            return 0
        return node.val + self.total(node.left) + self.total(node.right)
    
    def prod(self, node):
        if node is None:
            return 0
        L, R = self.prod(node.left), self.prod(node.right)
        
        curr = L + R + node.val
        self.res = max(self.res, curr * (self.total_val - curr))
        
        return curr
        
    
    def maxProduct(self, root: TreeNode) -> int:
        self.total_val = self.total(root)
        
        self.res = 0
        
        self.prod(root)
        
        return self.res % int(1e9 + 7)