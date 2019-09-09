# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion, using BST property
class Solution:
    def dfs(self, node, p_val, q_val):
        if node.val < p_val and node.val < q_val:
            return self.dfs(node.right, p_val, q_val)
        if node.val > p_val and node.val > q_val:
            return self.dfs(node.left, p_val, q_val)
        return node
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p.val, q.val)

# Solution 1.1, similar idea, but using iteration
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr

# Solution 2, recursion, applicable to binary tree
class Solution:
    def dfs(self, node, p, q):
        if node is None or node is p or node is q:
            return node
        
        L, R = self.dfs(node.left, p, q), self.dfs(node.right, p, q)
        
        if L is None:
            return R
        if R is None:
            return L
        
        return node
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)