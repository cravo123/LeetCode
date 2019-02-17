# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.dfs(p.left, q.right) and self.dfs(p.right, q.left)
        
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        return self.dfs(root.left, root.right)

# Iteration
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        
        q = [root.left, root.right]
        
        while q:
            R, L = q.pop(), q.pop()
            if L is None or R is None:
                if L is not R:
                    return False
                else:
                    continue
            if L.val != R.val:
                return False
            q.append(L.left)
            q.append(R.right)
            q.append(L.right)
            q.append(R.left)
        return True
