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
            return p == q
        
        return p.val == q.val and self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
        
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        return self.dfs(p, q)

# Iteration
class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        curr = [[p, q]]
        
        while curr:
            p, q = curr.pop()
            if p is None or q is None:
                if p is not q:
                    return False
                continue
            if p.val != q.val:
                return False
            curr.append([p.left, q.left])
            curr.append([p.right, q.right])
        return True
