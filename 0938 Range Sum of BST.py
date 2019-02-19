# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, low, high):
        if node is None:
            return 0
        if node.val < low:
            return self.dfs(node.right, low, high)
        if node.val > high:
            return self.dfs(node.left, low, high)
        return node.val + self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
    
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        return self.dfs(root, L, R)

# Iteration
class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        res = 0
        if root is None:
            return res
        
        q = [root]
        
        while q:
            p = q.pop()
            val = p.val
            
            if val < L and p.right:
                q.append(p.right)
            
            if val > R and p.left:
                q.append(p.left)
            
            if L <= val <= R:
                res += val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return res