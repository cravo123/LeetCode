# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node, curr):
        if node is None:
            return 0
        curr = curr * 10 + node.val
        if node.left is None and node.right is None:
            return curr
        
        return self.dfs(node.left, curr) + self.dfs(node.right, curr)
        
        
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

# Solution 1.1, recursion using global variable
class Solution:
    def dfs(self, node, curr):
        if node is None:
            return
        curr = curr * 10 + node.val
        
        if node.left is None and node.right is None:
            self.res += curr
        
        self.dfs(node.left, curr)
        self.dfs(node.right, curr)
        
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root, 0)
        
        return self.res