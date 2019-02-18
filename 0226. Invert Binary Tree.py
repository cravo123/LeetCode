# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return
        node.left, node.right = self.dfs(node.right), self.dfs(node.left)
        return node
    
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        return self.dfs(root)

# Iteration
class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        
        q = [root]
        
        while q:
            p = q.pop()
            
            p.left, p.right = p.right, p.left
            
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return root