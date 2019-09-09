# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
# return both new head and tail
class Solution:
    def dfs(self, node):
        if node is None:
            return None, None # head, tail
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if L[0] is None:
            node.left = None
            node.right = R[0]
            return node, R[1] if R[1] else node
        
        L[1].right = node
        node.left = None
        node.right = R[0]
        
        return L[0], R[1] if R[1] else node
        
        
    def increasingBST(self, root: 'TreeNode') -> 'TreeNode':
        res, _ = self.dfs(root)
        
        return res