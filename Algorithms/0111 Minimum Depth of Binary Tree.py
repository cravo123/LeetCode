# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        if node.left is None:
            return 1 + self.dfs(node.right)
        if node.right is None:
            return 1 + self.dfs(node.left)
        
        return 1 + min(self.dfs(node.left), self.dfs(node.right))
        
    def minDepth(self, root: 'TreeNode') -> 'int':
        return self.dfs(root)

# Solution 2, iteration
# if we do level traversal, and find a node which has no children, 
# then it represents the minimum height
class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        level = 0
        if root is None:
            return level
        
        q = [root]
        while q:
            level += 1
            for p in q:
                if p.left is None and p.right is None:
                    return level
            q = [x for p in q for x in [p.left, p.right] if x]
