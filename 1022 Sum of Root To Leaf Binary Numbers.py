# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, use global variable to record result
class Solution:
    base = int(10**9) + 7
    def dfs(self, node, curr):
        if node is None:
            return
        curr = (curr * 2 + node.val) % self.base
        
        if node.left is None and node.right is None:
            self.res = (self.res + curr) % self.base
        self.dfs(node.left, curr)
        self.dfs(node.right, curr)
        
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        
        return self.res