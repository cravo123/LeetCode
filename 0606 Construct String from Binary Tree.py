# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return ''
        if node.left is None and node.right is None:
            return str(node.val)
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        L = '(%s)' % L
        R = '' if R == '' else '(%s)' % R
        
        return '%d%s%s' % (node.val, L, R)
    
    def tree2str(self, t: TreeNode) -> str:
        res = self.dfs(t)
        
        return res