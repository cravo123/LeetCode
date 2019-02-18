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
            return 0
        curr = 0
        if node.left and node.left.left is None and node.left.right is None:
            curr += node.left.val
        curr += self.dfs(node.left) + self.dfs(node.right)
        
        return curr
        
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        return self.dfs(root)

# Iteration
class Solution:
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        res = 0
        if root is None:
            return res
        
        q = [root]
        
        while q:
            tmp = []
            
            for p in q:
                if p.left and p.left.left is None and p.left.right is None:
                    res += p.left.val
                
                if p.left:
                    tmp.append(p.left)
                if p.right:
                    tmp.append(p.right)
            q = tmp
        return res