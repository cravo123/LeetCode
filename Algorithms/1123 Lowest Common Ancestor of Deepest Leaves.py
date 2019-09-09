# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
# Use the trick to return 2 values, so O(n)
class Solution:
    def dfs(self, node):
        if node is None:
            return 0, None
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if L[0] > R[0]:
            return L[0] + 1, L[1]
        if L[0] < R[0]:
            return R[0] + 1, R[1]
        
        return L[0] + 1, node
        
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        res = self.dfs(root)
        
        return res[1]

# Solution 2, calculate height
# Two recursions, O(n^2)
# one to calculate height, 
# one to get lowest common ancestor node
class Solution:
    def height(self, node):
        if node is None:
            return 0
        L, R = self.height(node.left), self.height(node.right)
        
        return max(L, R) + 1
    
    def dfs(self, node):
        if node is None:
            return
        l_h, r_h = self.height(node.left), self.height(node.right)
        l_n, r_n = self.dfs(node.left), self.dfs(node.right)
        
        if l_h > r_h:
            return l_n
        if r_h > l_h:
            return r_n
        return node
    
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)